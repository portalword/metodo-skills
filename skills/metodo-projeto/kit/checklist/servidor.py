"""
Checklist ao vivo do ROADMAP (metodo-projeto).

Uso:  python servidor.py "C:/caminho/do/projeto"  [porta]
Abre: http://127.0.0.1:8765  (a página atualiza sozinha)

- Lê os itens "- [ ] 1.2 texto" / "- [x] ..." / "- [-] ..." (pela metade) do ROADMAP.md do projeto (títulos "## ..." viram seções).
- Clicar no item na página marca/desmarca direto no ROADMAP.md (a IA vê na hora).
- Comentários/perguntas do usuário vão para CHECKLIST-COMENTARIOS.md (a IA lê e responde ali).
Só usa a biblioteca padrão do Python. Escuta só em 127.0.0.1 (ninguém de fora acessa).
"""
import json, re, sys, os, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
ROADMAP = os.path.join(ROOT, "ROADMAP.md")
NOTES = os.path.join(ROOT, "CHECKLIST-COMENTARIOS.md")
REGRAS = os.path.join(ROOT, "design", "REGRAS.md")
FUTUROS = os.path.join(ROOT, "PLANOS-FUTUROS.md")  # criado pela skill design-sistema
SUBS = os.path.join(ROOT, "SUBAGENTS.json")  # config dos subagents (aba Subagents)
SUBS_PADRAO = {"critico-visual": {"nome": "Crítico visual", "ativo": True, "limite": 0, "modelo": "sonnet",  # limite 0 = sem limite
                                   "opcoes": {"aprovaInterface": False, "aprovaEntrega": False}},
               "testador": {"nome": "Testador", "ativo": True, "limite": 3, "modelo": "sonnet",
                            "opcoes": {"aprovaFuncao": False, "testaEntrega": True, "semTestes": False}}}
MODELOS = ("haiku", "sonnet", "opus")
CAMPOS = ("ativo", "limite", "modelo", "opcoes")
HISTS = {"critico-visual": os.path.join(ROOT, "CRITICO-HISTORICO.md"), "testador": os.path.join(ROOT, "TESTADOR-HISTORICO.md")}  # rodadas: '### <passo> · <data> · <aprovado|recusado>' + 'Resumo: ...' + texto
PAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checklist.html")
ITEM = re.compile(r"^(\s*)- \[( |x|X|-)\] (.*)$")  # [-] = pela metade / precisa de outro passo


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def parse():
    """Devolve seções com itens: [{titulo, itens:[{linha, feito, texto, id}]}]"""
    secs, cur = [], None
    for i, line in enumerate(read(ROADMAP).splitlines()):
        if line.startswith("#"):
            cur = {"titulo": line.lstrip("#").strip(), "itens": []}
            secs.append(cur)
            continue
        m = ITEM.match(line)
        if m:
            if cur is None:
                cur = {"titulo": "", "itens": []}
                secs.append(cur)
            txt = m.group(3).strip()
            num = re.match(r"^(\d+(\.\d+)*)\s", txt)
            cur["itens"].append({"linha": i, "feito": m.group(2).lower() == "x", "meio": m.group(2) == "-", "texto": txt, "id": num.group(1) if num else txt[:40]})
    return [s for s in secs if s["itens"]]


def contrato():
    """Bloco '## Contrato' do ROADMAP: linhas '- **Parte:** texto' (ou '**Parte:** texto') + linha 'Plano aprovado em'."""
    partes, dentro, atual, aprovado = {}, False, None, ""
    for line in read(ROADMAP).splitlines():
        if "aprovado em" in line.lower() and line.lstrip().startswith(">"):
            aprovado = line.lstrip("> ").strip()
        if line.startswith("## "):
            dentro = line[3:].strip().lower().startswith("contrato"); atual = None; continue
        if not dentro:
            continue
        m = re.match(r"^\s*(?:[-*]|\d+\.)?\s*\*\*(.+?):?\*\*:?\s*(.*)$", line)
        if m:
            atual = m.group(1).strip().rstrip(":"); partes[atual] = m.group(2).strip()
        elif atual and line.strip():
            partes[atual] = (partes[atual] + "\n" + line.strip()).strip()
    return {"partes": partes, "aprovado": aprovado}


def subs():
    try:
        cfg = json.loads(read(SUBS) or "{}")
    except ValueError:
        cfg = {}
    out = {}
    for k, v in SUBS_PADRAO.items():
        c = json.loads(json.dumps(v)); salvo = cfg.get(k, {})
        c["ativo"] = salvo.get("ativo", c["ativo"]); c["limite"] = salvo.get("limite", c["limite"])
        c["modelo"] = salvo.get("modelo") if salvo.get("modelo") in MODELOS else c["modelo"]
        c["opcoes"].update({o: bool(x) for o, x in salvo.get("opcoes", {}).items() if o in c["opcoes"]})
        out[k] = c
    return out


def atual():
    """O que cada subagent está fazendo agora (gravado por texto.py agente ...)."""
    try:
        d = json.loads(read(os.path.join(ROOT, "SUBAGENTS-ATUAL.json")) or "{}")
        return {k: {"estado": str(v["estado"]), "passo": str(v["passo"]), "desde": float(v["desde"])} for k, v in d.items() if k in SUBS_PADRAO}
    except (ValueError, KeyError, TypeError, AttributeError):
        return {}


def historico(quem):
    """Rodadas do subagent, mais recentes primeiro."""
    out, cur = [], None
    for line in read(HISTS[quem]).splitlines():
        m = re.match(r"^### (.+?) · (.+?) · (aprovado|recusado|sem-teste|aceito|precisa-de-voce)(?=\s|$).*$", line)
        if m:
            cur = {"passo": m.group(1), "quando": m.group(2), "resultado": m.group(3).lower(), "resumo": "", "texto": ""}
            out.append(cur)
        elif cur is not None:
            if line.startswith("Resumo:") and not cur["resumo"]:
                cur["resumo"] = line[7:].strip()
            else:
                cur["texto"] += line + "\n"
    for h in out:
        h["texto"] = h["texto"].strip()
    return out[::-1]


def notes():
    """Comentários: blocos '### <id> · <data>' com o texto abaixo; respostas da IA começam com '> IA:'."""
    out, cur = [], None
    for line in read(NOTES).splitlines():
        m = re.match(r"^### (.+?) · (.+)$", line)
        if m:
            cur = {"id": m.group(1), "quando": m.group(2), "texto": "", "resposta": "", "resolvido": False}
            out.append(cur)
        elif cur is not None:
            if line.startswith("> IA:"):
                cur["resposta"] += line[5:].strip() + " "
            elif line.strip() == "[resolvido]":
                cur["resolvido"] = True
            else:
                cur["texto"] += line + "\n"
    for n in out:
        n["texto"], n["resposta"] = n["texto"].strip(), n["resposta"].strip()
    return out


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, kind="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", kind + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            return self.send(200, read(PAGE), "text/html")
        if self.path == "/estado":
            nome = os.path.basename(ROOT)
            return self.send(200, json.dumps({"projeto": nome, "secoes": parse(), "notas": notes(), "mtime": os.path.getmtime(ROADMAP) if os.path.exists(ROADMAP) else 0}))
        if self.path == "/futuros":
            return self.send(200, json.dumps({"texto": read(FUTUROS)}))
        if self.path == "/contrato":
            return self.send(200, json.dumps(contrato()))
        if self.path == "/subagents":
            return self.send(200, json.dumps({"subs": subs(), "historicos": {k: historico(k) for k in HISTS}, "atual": atual()}))
        if self.path == "/design":
            return self.send(200, json.dumps({"texto": read(REGRAS)}))
        self.send(404, "{}")

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        data = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/marcar":
            lines = read(ROADMAP).splitlines()
            i = int(data["linha"])
            m = ITEM.match(lines[i]) if 0 <= i < len(lines) else None
            if not m:
                return self.send(409, json.dumps({"erro": "o ROADMAP mudou, recarregue"}))
            marca = {"feito": "x", "meio": "-"}.get(data.get("estado"), "x" if data.get("feito") else " ")
            lines[i] = f"{m.group(1)}- [{marca}] {m.group(3)}"
            with open(ROADMAP, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(lines) + "\n")
            return self.send(200, "{}")
        if self.path == "/subagents":
            cfg = subs(); k = data.get("id")
            if k not in cfg:
                return self.send(400, "{}")
            if "ativo" in data: cfg[k]["ativo"] = bool(data["ativo"])
            if "limite" in data: cfg[k]["limite"] = max(0, min(999, int(data["limite"] or 0)))
            if data.get("modelo") in MODELOS: cfg[k]["modelo"] = data["modelo"]
            if data.get("opcao") in cfg[k]["opcoes"]: cfg[k]["opcoes"][data["opcao"]] = bool(data.get("valor"))
            with open(SUBS, "w", encoding="utf-8", newline="\n") as f:
                json.dump({k: {x: v[x] for x in CAMPOS} for k, v in cfg.items()}, f, ensure_ascii=False, indent=2)
            return self.send(200, json.dumps(cfg))
        if self.path == "/comentar":
            txt = str(data.get("texto", "")).strip()
            if not txt:
                return self.send(400, "{}")
            quando = datetime.datetime.now().strftime("%d/%m %H:%M")
            head = "" if os.path.exists(NOTES) else "# Comentários do checklist\n\nPerguntas e pedidos do usuário por item. A IA responde com linhas '> IA: ...' e marca '[resolvido]'.\n"
            with open(NOTES, "a", encoding="utf-8", newline="\n") as f:
                f.write(f"{head}\n### {data.get('id', '?')} · {quando}\n{txt}\n")
            return self.send(200, "{}")
        self.send(404, "{}")


if __name__ == "__main__":
    if not os.path.exists(ROADMAP):
        print(f"Sem ROADMAP.md em {ROOT}")
    print(f"Checklist: http://127.0.0.1:{PORT}  (projeto: {ROOT})")
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()

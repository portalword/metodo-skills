"""
Versão em texto do checklist ao vivo (para IAs que não abrem navegador).

Uso:  python texto.py "<pasta do projeto>" <comando> [id] [texto]
Comandos: checklist | falta | feitos | atual | design | futuro | comentarios
          agente <critico-visual|testador> <analisando|corrigindo|parado> [passo]
          marcar <id> | metade <id> | desmarcar <id> | comentar <id> <texto>
Lê e escreve os mesmos arquivos da página (ROADMAP.md, CHECKLIST-COMENTARIOS.md, design/REGRAS.md, PLANOS-FUTUROS.md).
"""
import os, re, sys, datetime, json, time

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
CMD = (sys.argv[2] if len(sys.argv) > 2 else "checklist").lstrip("/").lower()
ARGS = sys.argv[3:]
ROADMAP = os.path.join(ROOT, "ROADMAP.md")
NOTES = os.path.join(ROOT, "CHECKLIST-COMENTARIOS.md")
REGRAS = os.path.join(ROOT, "design", "REGRAS.md")
FUT = os.path.join(ROOT, "PLANOS-FUTUROS.md")
ITEM = re.compile(r"^(\s*)- \[( |x|X|-)\] (.*)$")
ICON = {" ": "[ ]", "x": "[x]", "X": "[x]", "-": "[~]"}


def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def items():
    out, sec = [], ""
    for i, l in enumerate(read(ROADMAP).splitlines()):
        if l.startswith("#"):
            sec = l.lstrip("#").strip()
            continue
        m = ITEM.match(l)
        if m:
            t = m.group(3).strip()
            n = re.match(r"^(\d+(\.\d+)*)\s", t)
            out.append({"i": i, "sec": sec, "st": m.group(2), "t": t, "id": n.group(1) if n else t[:20]})
    return out


def show(filt):
    its = items()
    if not its:
        return print("Sem ROADMAP.md (ou sem itens) em", ROOT)
    feitos = sum(1 for x in its if x["st"] in "xX")
    meio = sum(1 for x in its if x["st"] == "-")
    atual = next((x for x in its if x["st"] not in "xX"), None)
    aprovado = "Plano aprovado" in read(ROADMAP)
    print(f"{os.path.basename(ROOT)} · {feitos}/{len(its)} feitos" + (f" · {meio} pela metade" if meio else "") + ("" if aprovado else " · PLANO AINDA NÃO APROVADO"))
    sec = None
    for x in its:
        if filt == "falta" and x["st"] in "xX":
            continue
        if filt == "feitos" and x["st"] not in "xX":
            continue
        if x["sec"] != sec:
            sec = x["sec"]
            print(f"\n**{sec}**")
        mark = " ← atual" if atual and x is atual else ""
        print(f"{ICON[x['st']]} {x['t']}{mark}")


def set_state(idv, st):
    lines = read(ROADMAP).splitlines()
    for x in items():
        if x["id"] == idv:
            m = ITEM.match(lines[x["i"]])
            lines[x["i"]] = f"{m.group(1)}- [{st}] {m.group(3)}"
            with open(ROADMAP, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(lines) + "\n")
            return print(f"{ICON[st]} {x['t']}")
    print("Item não encontrado:", idv)


def sections(path, empty):
    t = read(path)
    if not t.strip():
        return print(empty)
    for l in t.splitlines():
        if l.startswith("## "):
            print(f"\n**{l[3:].strip()}**")
        elif l.strip().startswith("- ") or (l.strip() and not l.startswith("#") and not l.startswith(">")):
            print(l.rstrip())


if CMD in ("checklist", "todos", "lista"):
    show("todos")
elif CMD == "falta":
    show("falta")
elif CMD in ("feitos", "feito"):
    show("feitos")
elif CMD in ("atual", "onde"):
    its = items()
    a = next((x for x in its if x["st"] not in "xX"), None)
    pend = [x for x in its if x["st"] in " -" and a and its.index(x) < its.index(a)]
    print("Atual:", a["t"] if a else "tudo feito")
    if pend:
        print("Pendentes antes dele:", ", ".join(x["id"] + (" (metade)" if x["st"] == "-" else "") for x in pend))
elif CMD == "design":
    sections(REGRAS, "Sem design/REGRAS.md neste projeto.")
elif CMD in ("futuro", "futuros"):
    sections(FUT, "Sem PLANOS-FUTUROS.md neste projeto.")
elif CMD in ("comentarios", "comentários"):
    t = read(NOTES)
    print(t.split("\n", 3)[-1].strip() if t.strip() else "Sem comentários.")
elif CMD == "agente" and len(ARGS) >= 2 and ARGS[0] in ("critico-visual", "testador") and (ARGS[1] == "parado" or (ARGS[1] in ("analisando", "corrigindo") and len(ARGS) > 2)):
    p = os.path.join(ROOT, "SUBAGENTS-ATUAL.json")
    try:
        d = json.loads(read(p) or "{}")
    except ValueError:
        d = {}
    d.pop(ARGS[0], None)
    if ARGS[1] != "parado":
        d[ARGS[0]] = {"estado": ARGS[1], "passo": " ".join(ARGS[2:]), "desde": time.time()}
    with open(p + ".tmp", "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False)
    os.replace(p + ".tmp", p)
    print(*ARGS)
elif CMD == "marcar" and ARGS:
    set_state(ARGS[0], "x")
elif CMD == "metade" and ARGS:
    set_state(ARGS[0], "-")
elif CMD == "desmarcar" and ARGS:
    set_state(ARGS[0], " ")
elif CMD == "comentar" and len(ARGS) >= 2:
    head = "" if os.path.exists(NOTES) else "# Comentários do checklist\n\nPerguntas e pedidos do usuário por item. A IA responde com linhas '> IA: ...' e marca '[resolvido]'.\n"
    with open(NOTES, "a", encoding="utf-8", newline="\n") as f:
        f.write(f"{head}\n### {ARGS[0]} · {datetime.datetime.now():%d/%m %H:%M}\n{' '.join(ARGS[1:])}\n")
    print("Comentário salvo em", ARGS[0])
else:
    print(__doc__)

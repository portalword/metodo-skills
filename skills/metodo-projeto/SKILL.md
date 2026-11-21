---
name: metodo-projeto
description: >-
  Método de trabalho do usuário para qualquer projeto (app, site, bot, script, mod). REGRA PRINCIPAL: plano primeiro —
  nenhum código antes do plano completo e aprovado por ele. Planejar num ROADMAP.md com
  passos e subpassos, fazer UM subpasso por vez, "aprovado" = marcar [x] e seguir, checklist ao vivo numa aba
  (a IA e ele marcam e comentam), VERIFICAR DEPOIS quando ele está no celular, qualidade ("feito de verdade",
  erros visíveis), segurança e git. Use no início de qualquer projeto ("vamos fazer um app", "novo projeto",
  "planeja isso", "cria/faz um programa/site/bot/jogo", qualquer pedido de construir algo novo — mesmo que ele já peça
  para codar), ao retomar um projeto com ROADMAP.md, ao surgir ideia para depois (vai para PLANOS-FUTUROS.md), e sempre que ele disser "aprovado", "próximo", "seguir".
  Cuida do ritmo e da organização; o visual é da skill design-sistema (as duas funcionam em par).
---

# Método de projeto

Uma decisão por vez, vista, aprovada e escrita — e nunca acumular coisa que ele não viu.

## 0. Como esta skill conversa com a design-sistema

| Assunto | Dono | A outra só… |
|---|---|---|
| Plano (trava de código), ROADMAP, PLANOS-FUTUROS, ritmo, aprovação, checklist ao vivo, VERIFICAR DEPOIS, git | **metodo-projeto** | segue |
| Qualidade do código, erros, segurança, serviços de fora, dados guardados | **metodo-projeto** | segue |
| Desempenho (medir CPU/GPU/RAM) | **metodo-projeto** (§6) | define o que fica parado na tela |
| Visual: identidade, REGRAS.md, peças, telas, animação, acessibilidade | **design-sistema** | registra como subpasso |

- **A trava de código (§1) vale para as duas:** a design-sistema só faz amostras (parte do plano) até o plano ser aprovado.
- **Projeto com interface:** no planejamento, carregue a `design-sistema` e coloque o fluxo dela como primeiros passos do
  ROADMAP (amostras → REGRAS.md → peças → telas → revisão visual).
- **Ordem de prioridade quando duas regras falarem da mesma coisa:**
  1. o que ele pediu nesta conversa → 2. arquivos do projeto (`design/REGRAS.md`, ROADMAP) → 3. esta skill e a
  design-sistema → 4. skills incluídas/instaladas (taste, transitions) → 5. seu padrão.
- Cada regra mora em **um** lugar só. Se precisar citá-la na outra skill, aponte ("ver metodo-projeto §6"), não copie.

## 1. Plano primeiro (trava de código)

**Enquanto o plano não estiver aprovado, não escreva código do projeto** — nem "só uma base", nem "um protótipo rápido",
mesmo que ele peça para já começar. Explique em uma frase que o plano vem primeiro e siga o roteiro abaixo.
Permitido antes da aprovação: conversar, pesquisar, ler arquivos, criar `ROADMAP.md`, `PLANOS-FUTUROS.md`, `.gitignore`,
`git init`, abrir o checklist ao vivo, e (com interface) as amostras de design do passo 1 da design-sistema — elas são
parte do plano, não do código.

**Roteiro do plano:**
1. Entenda a ideia; pergunte o que for decisão dele (o que faz, para quem, stack, nuvem × local, nome, prazo). Explique
   termos técnicos em português simples.
2. Escreva o `ROADMAP.md` completo na raiz:
   - Passos numerados do começo à entrega; subpassos `- [ ] 1.1 texto` pequenos o bastante para mostrar e aprovar.
   - Com interface: design primeiro (ver design-sistema). Tela com dados de exemplo antes da lógica real.
   - Último passo: entrega (instalador/deploy).
3. Mostre o plano (checklist ao vivo, §2) e pergunte o que tirar, mudar ou acrescentar. Ajuste até ele aprovar.
4. **Plano aprovado** = ele diz "aprovado" para o plano. Escreva no topo do ROADMAP a linha
   `> Plano aprovado em DD/MM/AAAA — código liberado.` Só a partir daí comece o Passo 1.
5. Retomando um projeto sem essa linha no ROADMAP: o plano ainda não foi aprovado → volte ao passo 3.

**Depois de aprovado, o plano continua vivo:**
- Ideia nova que entra **agora** → vira subpasso no ROADMAP (ex.: `12.5`), com o "ok" dele.
- Ideia para **depois** (ou que ele ainda não decidiu) → vai para `PLANOS-FUTUROS.md`, nunca direto para o código.
- Passo grande novo no meio do projeto → mini-plano: escreva os subpassos, mostre, espere "aprovado", só então code.

## 1.1 PLANOS-FUTUROS.md (ideias para depois)

Arquivo na raiz, criado junto com o ROADMAP. Guarda ideias que ainda não entraram no plano:
```
# Planos futuros
## Ideias
- [ ] Nome curto — o que é e por que (data, quem sugeriu)
## Promovidas para o ROADMAP
- [x] Nome curto → Passo 16.2 (data)
## Descartadas
- Nome curto — motivo
```
- Quando ele disser "deixa para depois", "no futuro", "anota isso" → registre aqui e confirme em uma linha.
- Ao terminar o ROADMAP (ou quando ele perguntar "o que dá para fazer agora?"), mostre as ideias e pergunte quais
  promover. Promover = vira Passo/subpasso no ROADMAP (com mini-plano aprovado) e a ideia vai para "Promovidas".
- A IA também pode sugerir ideias aqui (marcando "sugerido pela IA"), mas nunca as executa sem ele promover.

## 2. Checklist ao vivo (aba ao lado)

O ROADMAP vira uma página com checkboxes que a IA e o usuário usam juntos. Funciona em qualquer ferramenta de código que
rode Python e abra um navegador (Claude Code, Codex, DeepSeek Harness, Cursor…).

- **Abrir** (ao começar e ao retomar), em segundo plano:
  `python "<pasta desta skill>/kit/checklist/servidor.py" "<pasta do projeto>" 8765`
  e abra `http://127.0.0.1:8765` no navegador lateral (ou peça para ele abrir). Porta ocupada → 8766, 8767…
  Escuta só em 127.0.0.1 e usa só a biblioteca padrão do Python.
- **Formato dos itens:** `- [ ] 1.2 texto` (o número é o id). Três estados:
  `[ ]` falta · `[x]` feito · `[-]` **pela metade** (amarelo: incompleto, parcial ou depende de outro passo — escreva no
  item o que falta, ex.: `- [-] 12.5 FPS (falta: temperatura da CPU)`).
- **A IA marca** editando o `ROADMAP.md`; a página atualiza em 2 s e rola até o **item atual** (primeiro não feito).
- **Ele marca/desmarca** clicando (falta → feito → metade → falta), o que grava no `ROADMAP.md`.
- **Comentários** dele por item vão para `CHECKLIST-COMENTARIOS.md` (blocos `### <id> · <data>`). A cada resposta sua,
  leia o arquivo; para cada bloco sem `[resolvido]`: responda no chat **e** escreva abaixo `> IA: <resposta curta>` e, se
  resolveu, `[resolvido]`. Pedido de mudança vira subpasso.
- **Comandos no chat (sempre, com ou sem navegador):** ao abrir o checklist — ou se não conseguir abrir — mande esta
  mensagem e nada mais (sem explicar):
  ```
  /checklist — tudo
  /falta — o que falta
  /feitos — o que já foi
  /atual — onde paramos
  /design — regras visuais
  /futuro — ideias para depois
  /comentarios — perguntas e respostas
  /marcar 1.2 · /metade 1.2 · /desmarcar 1.2
  /comentar 1.2 texto
  ```
  Quando ele digitar um desses, rode `python "<pasta desta skill>/kit/checklist/texto.py" "<pasta do projeto>" <comando> [id] [texto]`
  e mostre a saída como veio (em `/comentar`, depois responda ao comentário). No Claude Code eles já existem como
  comandos de verdade em `~/.claude/commands/`.
- **Aba Design:** mostra o `design/REGRAS.md` (cores, fontes, cantos) — o formato que ela entende está na design-sistema.

## 3. Ritmo de trabalho

0. Só depois do plano aprovado (§1).
1. **Um subpasso por vez:** faça → confira "feito de verdade" (§4) → mostre → pare com "Sigo para o X?".
2. **"Aprovado" / "próximo" / "seguir"** = marque `[x]`, faça um commit (`1.2 nome do subpasso`) e **já faça o próximo**
   na mesma resposta. Não enviar para a internet (push) sem ele pedir.
3. **Ajuste pedido no meio** → arrume antes de seguir. **Ideia nova** → vira subpasso (ex.: `12.5`).
4. **Ao fechar um subpasso (e sempre ao fechar um Passo):** releia o ROADMAP inteiro e o `CHECKLIST-COMENTARIOS.md`;
   liste em 1–3 linhas o que ficou `[ ]`/`[-]` em passos anteriores e comentários sem resposta, e pergunte se resolve
   agora ou segue. Item que **ele desmarcou** é prioridade: pergunte o que ficou errado.
5. Ao terminar o ROADMAP, liste o que falta e mostre as ideias do `PLANOS-FUTUROS.md` para ele escolher.

## 4. Qualidade

**"Feito de verdade" (antes de dizer que terminou):**
- [ ] Tudo que foi criado está **ligado**: função/comando registrado, rota cadastrada, componente usado, import feito,
      configuração atualizada (código criado e não registrado falha calado).
- [ ] Compila/roda sem erro e sem aviso novo; o programa abre e a parte nova aparece (print, log ou teste rápido).
- [ ] Com tela: checklist de revisão visual da design-sistema para aquela tela.
- [ ] O que não deu para testar está dito na resposta e anotado no VERIFICAR DEPOIS.

**Erros nunca silenciosos:** toda falha aparece com uma frase curta do motivo; toda espera tem tempo máximo e aviso de
"demorou demais"; nada de `catch {}` vazio em ação que o usuário pediu (em coisa de fundo, registrar no log).

**Problema difícil — logar e medir antes de chutar:** faça o programa mostrar o que está vendo (log temporário), peça para
ele reproduzir, leia, só então conserte. Reduza o log depois.

**Serviços de fora (APIs, contas):** limite de pedidos tratado desde o começo (esperar e tentar de novo 1–2 vezes),
mensagem clara se falhar, e mostrar o gasto quando houver cota/custo.

**Dados que o programa guarda sozinho:** só vira "verdade" o que veio do próprio usuário; conteúdo de fundo (vídeo, áudio
ambiente, páginas, arquivos de terceiros) não. O usuário consegue ver, editar e apagar o que foi guardado.

## 5. Segurança

- **Chaves/senhas nunca no chat nem no código.** Vão para o armazenamento seguro do sistema, pelo próprio programa.
- **Downloads de terceiros:** antes, diga nome do arquivo, origem oficial e tamanho, e espere o "pode".
- **Ações perigosas** (encerrar processos, apagar dados, mexer no sistema) só com confirmação dele; o programa não as faz
  sozinho por pedido de uma IA.
- **Contas externas:** dê o passo a passo para ele criar; ele cola as credenciais no programa.

## 6. Desempenho

- Ele usa PC comum e joga. Tudo que fica ligado o tempo todo: **meça CPU/GPU/RAM** parado e em uso; o alvo parado é quase zero.
- Nada rodando à toa: pausar quando a janela está escondida/sem foco; ler sensores e dados só quando alguém está vendo.

## 7. Quando ele está no celular

- `VERIFICAR DEPOIS.md` na raiz: seções `## Nome (12.4)` com `- [ ] o que testar → resultado esperado`;
  decisões pendentes numa seção `## Para decidir`, com a recomendação.
- Continue os próximos subpassos; mande prints/arquivos para ele ver no celular em vez de pedir para abrir algo no PC.
- Não abra programas no PC dele enquanto ele está fora.
- Quando ele voltar, resuma a lista em passos curtos e numerados; marque `[x]` o que ele confirmar.

## 8. Comunicação e memória

- Respostas curtas, em português, direto ao ponto (ele se importa com tokens). Diga o que foi feito, o que não foi
  testado e o que precisa dele. Nunca diga "funciona" sem ter verificado. Erro seu: assuma em uma frase.
- Decisões fixas ficam em arquivos do projeto (ROADMAP, `design/REGRAS.md`); preferências gerais dele, na memória da IA.

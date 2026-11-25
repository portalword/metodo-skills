---
name: metodo-projeto
description: >-
  Método de trabalho do José para qualquer projeto (app, site, bot, script, mod). REGRA PRINCIPAL: plano primeiro —
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
1. **Pergunte bastante.** Enquanto estiver em plano, faça perguntas em rodadas (3–6 por vez, numeradas) até cobrir
   tudo, e só pare quando **ele disser "plano finalizado"**. Até lá, cada resposta termina com novas perguntas.
   **Formato de cada pergunta** (a interpretação pode ser difícil):
   ```
   1. Pergunta curta e simples?

      Explicação: o que essa pergunta quer saber e por quê (uma linha, com exemplo se ajudar).
   ```
   Entenda a ideia; pergunte o que for decisão dele (o que faz, para quem, stack, nuvem × local, nome, prazo). Explique
   termos técnicos em português simples.
2. **Contrato do plano.** A **primeira mensagem** dele ("quero fazer um app que…") vira a parte **Ideia**. As perguntas
   seguintes preenchem o resto do bloco `## Contrato` no topo do `ROADMAP.md` (uma linha por parte, no formato
   `- **Parte:** texto`, que a aba **Contrato** do checklist mostra numa folha). A lacuna de cada parte vira a próxima
   pergunta; o plano está completo quando nenhuma estiver vazia:
   1. **Ideia:** o que entregar e o nível de qualidade, em um parágrafo.
   2. **Prioridades:** lista em ordem, usada quando duas coisas brigam.
   3. **Restrições:** o que é proibido ou obrigatório (tecnologias, arquivos, privacidade, custo).
   4. **Alvo:** números no lugar de adjetivos (máquina/aparelho, tempo de abertura, tamanho, FPS, preço).
   5. **Escopo:** tudo que o produto tem, em itens (telas, funções). Nada de "bonito", "rápido".
   6. **Controles:** só quando o produto precisa (jogo, app com atalhos) ou ele pedir; senão, nem pergunte.
   7. **Verificação:** como cada coisa será conferida (teste, medida, crítico visual da design-sistema).
   8. **Pronto quando:** condições medíveis + lista de entregas com nome.
   9. **Ambiente:** onde roda e com quais ferramentas.
   Em planos seguintes (Plano 2…), a prioridade 1 é sempre "não quebrar o que já funciona", medindo antes e depois.
3. Com o Contrato aprovado ("plano finalizado"), gere o checklist **a partir dele**: cada subpasso cita a parte do
   Contrato que cumpre e tem seu "pronto quando" em uma linha. Escreva o `ROADMAP.md` completo na raiz:
   - Passos numerados do começo à entrega; subpassos `- [ ] 1.1 texto` pequenos o bastante para mostrar e aprovar.
   - Com interface: design primeiro (ver design-sistema). Tela com dados de exemplo antes da lógica real.
   - **Último passo é sempre `Entrega`**, com estes subpassos fixos:
     1. **Teste rápido de cada função** do Escopo (uma conferida curta por função, sem bateria longa;
        com `testaEntrega`, quem faz é o Testador, §4.1).
     2. **Teste rápido de interface:** prints de cada tela → **crítico visual** (design-sistema §8: prints + `Passo · o que é`;
        ele lê Contrato e REGRAS sozinho e recusa qualquer defeito). Corrija tudo até aprovar.
     3. **Conferir problemas:** releia Contrato e checklist, resolva `[ ]`/`[-]` que sobraram, comentários sem resposta.
     4. **Empacotar:** instalador/deploy + lista de entregas do "Pronto quando".
4. Mostre o plano (checklist ao vivo, §2) e pergunte o que tirar, mudar ou acrescentar. Ajuste até ele aprovar.
5. **Plano aprovado** = ele diz "aprovado" para o plano. Escreva no topo do ROADMAP a linha
   `> Plano aprovado em DD/MM/AAAA — código liberado.` Só a partir daí comece o Passo 1.
6. Retomando um projeto sem essa linha no ROADMAP: o plano ainda não foi aprovado → volte ao passo 4.

**Contrato assinado = travado.** Depois de "plano finalizado"/"aprovado", o Contrato não muda até o próximo plano:
- **Pode (ajuste):** mexer na forma do que está sendo feito ou já foi aprovado — trocar botão de lugar, pôr um botão ali,
  refazer o layout de uma tela, cor, texto, "não aprovado, muda isso".
- **Pode (remover):** tirar uma função do plano. Marque `- [x] 3.1 ~~texto~~ (removido)` e siga para a próxima.
- **Não pode (trocar):** pôr uma função nova no lugar ou em cima de outra ("não quero mais a 3.1, quero a função X").
  Diga em uma frase que muda o Contrato, anote em `PLANOS-FUTUROS.md` para o próximo plano e siga o atual.
- Na dúvida: se muda o Escopo ou as Prioridades do Contrato, é troca; se cabe no subpasso atual, é ajuste.

**Depois de aprovado, o plano continua vivo:**
- Ajuste pedido agora (ver acima) → vira subpasso no ROADMAP (ex.: `12.5`), com o "ok" dele.
- Ideia para **depois** (ou que ele ainda não decidiu) → vai para `PLANOS-FUTUROS.md`, nunca direto para o código.

**Fim de um plano → próximo:** cada Contrato tem o seu Checklist (Contrato 1 ↔ Checklist 1, Contrato 2 ↔ Checklist 2…).
Com tudo `[x]`, pergunte se haverá outro plano. Se sim: rode `texto.py "<projeto>" novo-plano` (guarda ROADMAP, comentários
e históricos em `planos/N/` e cria o `ROADMAP.md` novo) e siga o mesmo roteiro, com **os passos começando em 1**, puxando o
`PLANOS-FUTUROS.md`. Planos guardados são só leitura: abra só se precisar de algo de lá. Projeto antigo com `# Plano 2` no
mesmo arquivo continua assim até terminar; não renumere.

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
- **A IA marca** editando o `ROADMAP.md`; a página atualiza em 2 s e destaca o **item atual** (o botão de alvo leva até ele).
- **Ele marca/desmarca** clicando (falta → feito → metade → falta), o que grava no `ROADMAP.md`.
- **Comentários** dele por item vão para `CHECKLIST-COMENTARIOS.md` (blocos `### <id> · <data>`). A cada resposta sua,
  leia o arquivo; para cada bloco sem `[resolvido]`: responda no chat **e** escreva abaixo `> IA: <resposta curta>` e, se
  resolveu, `[resolvido]`. Pedido de ajuste vira subpasso; troca de função vai para `PLANOS-FUTUROS.md` (§1).
- **Aba Agentes:** liga/desliga cada subagent e define limite de rodadas (ou sem limite); grava em `SUBAGENTS.json`.
  Leia esse arquivo antes de chamar qualquer subagent listado ali (crítico visual: design-sistema §8; Testador: §4.1).
- **Comandos no chat (sempre, com ou sem navegador):** ao abrir o checklist — ou se não conseguir abrir — mande esta
  mensagem e nada mais (sem explicar):
  ```
  /abrir-checklist — abre a página (/open-checklist)
  /checklist — tudo
  /falta — o que falta (/todo)
  /feitos — o que já foi (/done)
  /atual — onde paramos (/current)
  /design — regras visuais
  /futuro — ideias para depois (/future)
  /comentarios — perguntas e respostas (/comments)
  /marcar 1.2 · /metade 1.2 · /desmarcar 1.2 (/check · /half · /uncheck)
  /comentar 1.2 texto (/comment)
  /detalhes 1.2 — mais detalhes (/details)
  ```
  Comando em inglês = o mesmo em português (todo→falta, done→feitos, current→atual, future→futuro, comments→comentarios,
  check→marcar, half→metade, uncheck→desmarcar, comment→comentar, details→detalhes). `/detalhes [passo]` não usa o
  `texto.py`: a IA explica o passo (ou a última resposta) sem o limite de 8 linhas e depois volta ao curto. `/abrir-checklist` = seção "Abrir" acima.
  Quando ele digitar um desses, rode `python "<pasta desta skill>/kit/checklist/texto.py" "<pasta do projeto>" <comando> [id] [texto]`
  e mostre a saída como veio (em `/comentar`, depois responda ao comentário). No Claude Code eles já existem como
  comandos de verdade em `~/.claude/commands/`.
- **Aba Design:** mostra o `design/REGRAS.md` (cores, fontes, cantos) — o formato que ela entende está na design-sistema.

## 3. Ritmo de trabalho

0. Só depois do plano aprovado (§1).
   **Antes de cada subpasso, releia nesta ordem:** o `## Contrato` (fonte da verdade), o checklist do `ROADMAP.md` (onde
   paramos) e o `PLANOS-FUTUROS.md` (o que NÃO entra agora). Mensagens antigas do chat são só apoio; se brigarem com o
   Contrato, vale o Contrato.
1. **Um subpasso por vez, nesta ordem (nunca em paralelo):**
   **fazer → conferir (§4) → Crítico, se tem tela (design-sistema §8) → Testador, se tem função (§4.1) → fechar.**
   - Recusou → o desenvolvimento corrige **tudo** → volta ao **mesmo tipo** de agente para confirmar → até aprovar ou bater
     o limite.
   - O Testador só entra depois do crítico aprovar. Se a correção do Testador mudar a tela, o crítico confere só essa mudança.
   - Enquanto um agente analisa, **não mude os arquivos do projeto** nem comece o próximo.
   - Todos os que se aplicam aprovaram com o botão ligado (`aprovaInterface` / `aprovaFuncao` / `aprovaEntrega`) = aprovado
     pelo usuário: feche e **faça o próximo na mesma resposta, sem perguntar**. Senão, mostre e pare com "Sigo para o X?".
2. **Fechar** (ou "aprovado" / "próximo" / "seguir") = marque `[x]` e faça **um** commit (`1.2 nome do subpasso`; sem commit
   de "aguardando"). Não enviar para a internet (push) sem ele pedir.
3. **Ajuste pedido no meio** → arrume antes de seguir. **Ideia nova** → `PLANOS-FUTUROS.md` (Contrato travado, §1).
4. **Ao fechar um subpasso (e sempre ao fechar um Passo):** releia o ROADMAP inteiro e o `CHECKLIST-COMENTARIOS.md`;
   liste em 1–3 linhas o que ficou `[ ]`/`[-]` em passos anteriores e comentários sem resposta, e pergunte se resolve
   agora ou segue (aprovado pelo crítico ou Testador: só liste e siga). Item que **ele desmarcou** é prioridade: pergunte o que ficou errado.
5. **Fechamento de cada subpasso (até 8 linhas, sempre assim):**
   ```
   ## 1.2 — Finalizado
   **O que foi feito:** (até 3 linhas simples)

   ## Próximo: 1.3 — (nome)
   **O que será feito:** (1 linha)
   ```
   Só entra mais uma linha se houver erro, algo não testado ou pergunta. Mais que isso, ele pede com `/detalhes`.
6. Ao terminar o ROADMAP, liste o que falta e mostre as ideias do `PLANOS-FUTUROS.md` para ele escolher.

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

## 4.1 Agentes: regras do Crítico e do Testador

Config em `SUBAGENTS.json` (aba Agentes); sem o campo: ativo, limite 3, `sonnet`, aprovações e `semTestes` desligados,
`testaEntrega` ligado. Releia antes de chamar **e** quando o resultado chegar. O crítico tem o resto na design-sistema §8.

**Os dois:**
- **Rodada 1** = completa. **Rodada 2 em diante** = agente novo que só **confirma**: confere a lista da última recusa (ele lê
  no arquivo de histórico) e o que a correção mexeu. Defeito novo causado pela correção também recusa.
- **Antes de chamar, sempre:** rode sozinho o comando de status com `analisando` e **espere a resposta**. Nunca chame o
  agente no mesmo lote. Respondeu `DESLIGADO` (ou erro) → não chame.
- **O desenvolvedor nunca explica.** Sem motivo, desculpa, o que mudou ou como deveria ser. Só responde corrigindo. Acha o
  agente errado? Quem decide é o usuário.
- **Limite** (`limite`; 0 = sem limite) ou 15 min presos no mesmo defeito → pare e mostre o que sobrou com 2 saídas. Só o
  usuário aceita (grave `aceito`). Nunca mude o teste para passar.
- **Status, sempre:** `python "<pasta desta skill>/kit/checklist/texto.py" "<projeto>" agente <critico-visual|testador>
  <analisando|corrigindo|parado> <passo>` — antes de chamar, ao receber recusa, e ao aprovar, cair ou esperar o usuário.
- **Histórico, assim que o resultado chega:** texto do agente sem mudar, em `CRITICO-HISTORICO.md` / `TESTADOR-HISTORICO.md`:
  ```
  ### 12.2 · DD/MM HH:MM · aprovado        (recusado · precisa-de-voce · sem-teste · aceito)
  Resumo: 9 casos, 0 defeitos.
  <texto completo>
  ```
- **Chat:** uma linha ao chamar (`Testando 12.2 — sigo sozinho quando o resultado chegar`) e uma ao recusar.
- **Não liberam** download, push, instalar, apagar, gastar, senha nem escolha entre opções.
- **Processos:** encerre só os que você abriu, pelo PID; nunca por nome (`taskkill /IM`).

**Testador** (agente fixo `testador`):
- Pedido **exato**: `Pasta: <caminho>` + `Passo X.Y` (rodada 2+: `Passo X.Y · confirmar`). Não aparece na lista de agentes?
  Diga a ele; não teste no lugar. Nunca mexa em `~/.claude/testador/`.
- `precisa-de-voce` → pare e mostre o que só ele pode testar. `ativo: false` → não chame; espere o "aprovado" dele.
- **Entrega** com `testaEntrega` → `Entrega` (+ passos sem teste: `Entrega · 12.2, 13.1`); desligado → teste rápido seu.
- **`semTestes: true`** (vence o resto, com o Testador ativo) → não chame; grave `sem-teste` com "Aprovado sem testar (botão
  ligado)." e siga. Nunca diga "testado". Na Entrega, liste os passos sem teste.

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
- **Chat curto (vale para toda resposta):** o detalhe mora nos arquivos e no checklist; o chat só avisa.
  - **Até 8 linhas.** Passe disso só em plano, perguntas, decisão difícil ou `/detalhes` (ou se ele pedir detalhe).
  - Um título `##`; listas com `-`, uma ideia por linha; tabela só se comparar 3 ou mais coisas; `---` só antes do que
    precisa dele. Sem subtítulos em resposta curta.
  - **Não escreva:** processo, lista de testes que passaram, texto dos agentes, opções do `SUBAGENTS.json`, o que já foi
    dito, nem "precisa de você: nada".
  - Agente (crítico/Testador): uma linha por resultado, ex.: `13.2 · Testador recusou: 1 defeito (pedido em inglês)`.
  - **Modelos fixos** (use o que couber, sem acrescentar blocos):
    - Subpasso: o fechamento da §3.
    - Agente rodando: `Testando 13.3 — sigo sozinho quando o resultado chegar`.
    - Recusado: `13.3 · Crítico recusou: 2 defeitos. Corrigindo.`
    - Pergunta ou erro: o que houve (1 linha) · opções (1 linha cada) · a pergunta.
    - Explicação pedida: resposta direta na 1ª linha, até 5 itens.
  - Números, commits, caminhos, portas e nomes internos só se ele precisar usar. Palavras simples.
  - Nunca corte: erro, algo não testado, risco ou pergunta para ele.
  - Entre ferramentas, fique calado; texto só para erro, demora ou mudança de rumo.

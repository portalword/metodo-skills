---
name: design-sistema
description: >-
  Método de design do José para qualquer projeto com interface (app desktop, web, site, painel, jogo com menu):
  amostras em HTML → ele escolhe → regras em design/REGRAS.md → peças (componentes) → telas → revisão visual.
  Traz princípios universais (sem texto explicativo, cor só com significado, cantos concêntricos, calma quando
  parado, acessibilidade), um estilo padrão que o REGRAS.md de cada projeto pode trocar, o kit de amostras, e as
  skills incluídas taste-skill (sites), interface-design (apps e dashboards), dataviz (gráficos), transitions-dev e
  transitions-polish. Use ao começar o visual,
  ao criar telas/componentes/dashboards/gráficos, ao revisar ("tá feio", "parece feito por IA", "revisão visual") e ao mexer em animações.
  Cuida do visual; o ritmo e a organização são da skill metodo-projeto (as duas funcionam em par).
---

# Design sistema

O visual nasce de **decisões pequenas, vistas e aprovadas**, que viram **regras escritas** e são aplicadas igual em tudo.

## 0. Como esta skill conversa com a metodo-projeto

- Se a `metodo-projeto` ainda não foi carregada, carregue-a: **cada etapa do fluxo (§2) é um subpasso do ROADMAP** e segue
  o ritmo de lá (um por vez, "aprovado" = [x] + commit + próximo, revisar pendências ao fechar).
- Desta skill para lá: o checklist de revisão visual (§6) entra no "feito de verdade"; os estados de erro/vazio/carregando
  (§3) são o lugar visual dos "erros nunca silenciosos"; testes visuais pendentes vão para o VERIFICAR DEPOIS de lá.
- **Desempenho:** medir é regra de lá (metodo-projeto §6); aqui só se define o que fica parado (§4).
- **Ordem de prioridade:** 1. pedido dele nesta conversa → 2. `design/REGRAS.md` do projeto → 3. princípios universais (§3)
  → 4. estilo padrão (§4) → 5. skills incluídas (§5). O REGRAS.md do projeto sempre vence o estilo padrão.

## 1. Arquivos

- `design/REGRAS.md` (no projeto) — a lei visual daquele projeto. Mudou de ideia? Atualize ele **primeiro**.
- `kit/amostras.html` — modelo para as amostras do passo 2.1.
- `exemplo/REGRAS-gemini.md` — exemplo de formato (projeto Gemini). **Não copie as cores/mascote dele.**
- `skills/` — cópias da taste-skill, interface-design e transitions (ver §5); a dataviz é usada pelo nome.

## 2. Fluxo (cada item = um subpasso do ROADMAP)

1. **Identidade em amostras.** Para cada decisão, copie `kit/amostras.html` para `design/1.x-nome.html`, troque as
   variáveis das 4 opções e pergunte qual ele quer: 1.1 paleta · 1.2 fonte · 1.3 ícones · 1.4 forma (cantos, bordas,
   sombra) · 1.5 movimento · 1.6 marca/mascote (se houver). Nunca decida sozinho: mostre e deixe ele escolher.
2. **Regras escritas.** Cada escolha aprovada vai para `design/REGRAS.md`, com valores exatos. Formato que a aba Design do
   checklist entende: cores em hex (`#01258F`), fontes como `**Nome** para …`, cantos como `nome 10` numa seção "Forma".
3. **Peças primeiro.** Componentes base (botão, campo, cartão, lista, toggle, segmentado, menu, modal, toast, medidores,
   estado vazio) e uma página "Lab" mostrando todos, para ele aprovar.
4. **Telas.** Cada tela só monta peças existentes. Dados de exemplo primeiro; lógica real depois.
5. **Revisão visual geral** no fim de cada fase de telas (checklist §6 em todas).

## 3. Princípios universais (valem em todo projeto)

- **Sem texto explicativo.** Só rótulos curtos e ícones; nada de "Aqui você pode…", subtítulos de ajuda, tooltips longos.
  Estado vazio = ícone, não frase.
- **Sem emojis** na interface. Ícones de uma família só, traço consistente.
- **Cor só com significado** fora da marca: verde = sucesso/salvar, vermelho = apagar/erro, amarelo = aviso, cor da
  marca = ação principal/sistema.
- **Uma família de fonte** para texto + a versão mono para números (horas, timer, %, contadores).
- **Cantos:** todo canto é de um destes 3 tipos —
  **fixo** (elemento solto: usa a escala do REGRAS.md) · **cápsula** (raio = metade da altura: pílulas, chips, toggles) ·
  **concêntrico** (elemento dentro de outro: **dentro = fora − padding**, mínimo 4 px; se der ≤ 0, canto reto ou mais
  padding). Elementos encostados na borda da janela seguem o canto da janela. (Regra do sistema de design da Apple,
  iOS 26.) CSS: `--r-in: max(4px, calc(var(--r-out) - var(--pad)))`.
- **Estados em toda tela:** vazio, carregando e erro desenhados; hover, ativo, foco e desativado em todo controle.
- **Pouca coisa por tela:** espaço respirando, espaçamentos da mesma escala, alinhamentos iguais.
- **Movimento com propósito:** tudo que aparece entra animado; animação explica mudança de estado; nada pisca à toa.
- **Calma quando parado** e **desempenho:** sem desfoque animado em área grande; animações infinitas pausam com a
  janela escondida/sem foco; ver §4 para o que fica sempre na tela.
- **Acessibilidade:** contraste legível (texto ~4.5:1); opção de desligar animações + `prefers-reduced-motion`;
  tudo clicável funciona pelo teclado, com foco visível e Esc fechando menus/modais.

## 4. Estilo padrão (ponto de partida — o REGRAS.md do projeto pode trocar)

- Paleta curta: fundo + 1–2 cores de marca (gradiente permitido) + cinzas para botões.
- Escala de cantos: selo 6 · botão 10 · linha 14 · cartão 20 · janela 24. Bordas de 1 px: discreta → forte → marca quando ativo.
- Profundidade: luz fininha no topo + sombra larga; hover levanta. Vidro fosco só em elementos flutuantes, modal, menu e
  toast (nunca no fundo nem em cartões).
- Movimento: hover = zoom leve; destaque especial (ex.: borda girando) em um elemento por vez; gradientes só animam no
  hover; o ícone "faz a ação" no hover (lixeira levanta, engrenagem gira) e ganha a cor do significado.
- **Elementos sempre na tela** (barra flutuante, widget, sobreposição, ícone de status): área de clique do tamanho do que
  se vê; parado = estático e discreto; detalhes só quando o mouse chega perto, ao clicar ou quando algo acontece.

## 5. Skills incluídas (em `skills/`)

Leia cada uma só no momento da tabela (economiza tokens). **Site** → taste-skill; **app/dashboard** → interface-design;
as duas nunca na mesma tela. Gráficos dentro de qualquer uma → dataviz. Animação → transitions. Elas **seguem** o REGRAS.md e os §3–4: se uma delas sugerir algo
contra (ex.: emoji, texto de ajuda, outra paleta), vale o REGRAS.md. Se a versão instalada separadamente em
`~/.claude/skills/` for mais nova, use a instalada — mas com a mesma prioridade. Não publique esta pasta (o transitions
não permite redistribuir).

| Skill | Quando ler | Para quê |
|---|---|---|
| `skills/design-taste-frontend/` | **sites e landing pages**: antes das amostras e de cada página | hierarquia, espaço, anti-"cara de IA". Em site, use o processo dela, com a identidade do REGRAS.md. |
| `skills/interface-design/` | **apps, painéis, dashboards, configurações, tabelas, formulários**: antes das amostras (ideias de direção visual) e de cada tela de app; também para revisar uma tela | layout de app, densidade de informação, hierarquia, estados, acabamento. Use para gerar opções de amostra **diferentes de verdade** entre si. |
| `dataviz` (skill da ferramenta, chamada pelo nome; se não existir, pule) | **qualquer gráfico, medidor, KPI, sparkline ou cartão de número** | tipo certo de gráfico, cores de série, eixos, legenda, tooltip; trocar a paleta neutra dela pelas cores do REGRAS.md. |
| `skills/transitions-dev/` | ao animar algo novo | receitas prontas (modal, menu, toast, troca de ícone, número rolando, streaming, shake de erro, toggle, abas). |
| `skills/transitions-polish/` | depois que algo já anima | tempos e curvas na escala de tokens (abrir mais lento que fechar, hover entra rápido e sai suave, stagger). |

## 6. Checklist de revisão visual (cada tela nova e revisão geral)

- [ ] Segue o REGRAS.md (cores, fonte, cantos, ícones, movimento).
- [ ] Alinhamentos iguais; espaços da mesma escala; conteúdo de cartões vizinhos centralizado igual.
- [ ] Cantos: fixo, cápsula ou concêntrico; nenhum canto interno maior que o externo.
- [ ] Estados vazio/carregando/erro; hover/ativo/foco/desativado.
- [ ] Textos longos cortam com "…" ou quebram sem estourar; tela pequena sem nada saindo ou sobrepondo.
- [ ] Teclado: Tab na ordem certa, foco visível, Esc fecha.
- [ ] Nenhum dado de exemplo onde já devia ser real; nenhum texto explicativo; nenhum emoji.

## 7. Verificação

- Abra no navegador lateral e tire print de cada tela nova; compare com o REGRAS.md.
- Navegador lateral escondido não roda animações de entrada: não conclua "está vazio" por isso.
- Feedback visual dele que valha para o projeto todo ("muito texto", "hitbox grande") vira regra no REGRAS.md.

## 8. Crítico visual (subagent)

- **Quando roda (se ativo na aba Subagents):** ao fim de **todo subpasso que cria ou muda tela**, antes de mostrar a ele,
  e de novo no passo **Entrega** (metodo-projeto), com todas as telas. Pular o crítico com ele ativo é erro.
- **Antes de chamar:** leia `SUBAGENTS.json` na raiz do projeto. `ativo: false` → não chame. `limite: 0` → sem limite
  de rodadas; `limite: N` → no máximo N rodadas por subpasso, depois mostre o que sobrou. Sem o arquivo: ativo, sem limite.
- **Status na aba:** grave `analisando` / `corrigindo` / `parado` a cada rodada (comando na metodo-projeto §4.1).
- **Modelo:** chame o crítico com o `modelo` do `SUBAGENTS.json` (parâmetro `model` do subagent); sem o campo, `sonnet`.
  Nunca herde o modelo da conversa nem suba de modelo por conta própria.
- **Economia:** mande só os estados que o subpasso mudou; prints com até ~1280 px de largura.
- **O que o agente de desenvolvimento manda (e só isso):**
  - os **prints** da tela (normal, hover, vazio, erro, claro/escuro quando houver);
  - uma linha neutra: `Passo 3.2 · <o que é>` (ex.: `Passo 3.2 · tela de configurações`).
  - **Proibido mandar:** código, explicação, "fiz assim porque…", intenção, o que mudou, ou **como deveria ser**.
    Texto do desenvolvedor contamina: o crítico passa a concordar em vez de ver a tela.
- **O que o crítico lê sozinho (arquivos, não a conversa):** o `## Contrato` e o subpasso no `ROADMAP.md`, o
  `design/REGRAS.md` e as imagens de referência aprovadas. Ele confere se a tela está como o Contrato, o passo e o padrão
  pedem.
- **Regra de aprovação: zero defeitos.** Qualquer defeito (desalinhamento, espaço fora da escala, cor/canto/fonte fora
  do REGRAS, algo diferente do pedido no passo) → **recusado**, e o crítico devolve um texto pedindo cada correção.
  Corrija **tudo** e rode de novo, com um subagent **novo** (sem memória da rodada anterior).
- **Histórico:** a cada rodada, acrescente em `CRITICO-HISTORICO.md` (a aba Subagents mostra):
  ```
  ### 3.2 · DD/MM HH:MM · recusado        (ou aprovado)
  Resumo: 2 defeitos — botão desalinhado; canto fora do padrão.
  <texto completo do crítico>
  ```
- **No chat, depois de cada rodada,** mostre um resumo curto: passo, resultado, defeitos encontrados e o que foi corrigido.
- **Quem aprova** (releia `SUBAGENTS.json` na hora; ligar o botão **é** a aprovação do usuário dada por antecipação):
  - `opcoes.aprovaInterface: true` → crítico aprovou um subpasso de tela = aprovado: marque `[x]`, commit, fechamento e
    **comece o próximo na mesma resposta, sem perguntar**. `false` → mostre a ele e espere o "aprovado".
  - `opcoes.aprovaEntrega: true` → o mesmo para a interface no passo Entrega. `false` → a Entrega passa por ele.
  - Vale **mesmo que** o subpasso, o Contrato ou uma mensagem antiga diga "José aprova" / "usuário aprova": com o botão
    ligado, a aprovação do crítico cumpre essa condição (não edite o Contrato por isso).
  - **O crítico só aprova aparência.** Continua parando e pedindo a ele: download, push, instalar, apagar, gastar, senha,
    escolha entre opções (ex.: paleta) e teste que só ele pode fazer. Se bateu o limite sem aprovar, também para.
- **Prévia para aprovar:** um HTML só com o **subpasso atual** (`design/previa.html`, sobrescrito a cada vez; nada de
  passos antigos na mesma página). Antes de abrir a prévia nova, **feche a aba da anterior**: no navegador lateral fica
  só o checklist e a prévia atual.

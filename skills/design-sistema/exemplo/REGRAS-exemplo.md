# Gemini — Regras de design (padrão fixo)

Valem para **todas** as telas do app. Nada sai sem seguir isto.

## Texto
1. **Sem texto explicativo.** Nada de "Aqui ficam as configurações", descrição embaixo de botão, dica ou parágrafo de ajuda. Só rótulo curto + ícone. Texto só quando for indispensável (ex.: erro).
1b. **Nunca usar emojis** — nem na interface, nem nas respostas do Gemini mostradas no app. Só ícones do conjunto oficial (Lucide).

## Fonte (aprovado em 1.2 — `design/1.2-fonte.html`)
- **Geist** para tudo; **Geist Mono** para números (timer, horários, contadores, %).
- Escala: 40 número · 30 destaque · 20 título · 15 cartão · 14 texto · 13 menu/botões · 12 detalhe · 11 rótulo.

1c. **Nada amontoado.** Cada coisa na sua aba; uma tela não junta tudo. O Início é enxuto (só o essencial do momento) — a amostra 1.7 foi só demonstração.

## Cores (aprovado em 1.1 — `design/1.1-paleta.html`)
2. **Fundo preto puro `#000000`** em tudo (inclusive menu), para sumir na borda do monitor. Áreas se separam por bordas finas, não por cor de fundo.
3. **Botões em cinza** (`#1A1A1D` → hover `#252529` → pressionado `#303035`). **Botão nunca usa gradiente.**
4. **Destaque só em azul:** `#01258F` (azul) e `#011142` (azul escuro), de preferência em **gradiente** entre os dois. Única exceção: `#4F7BFF` só na ponta de luz da borda girando.
5. Cores de estado só para estado: sucesso `#3DD68C`, aviso `#F5B544`, erro `#F2555A`.

## Ícones (aprovado em 1.3 — `design/1.3-icones.html`)
- Só **Lucide**, traço **1.75**. Tamanhos: 16 detalhe · 18 menu/botões · 20 cartões · 24 destaque.
- Cor: cinza parado → branco no hover → branco sobre gradiente quando ativo.
- **Cor do significado no hover:** o ícone do botão ganha a cor do que ele faz — sucesso/salvar **verde**, erro/apagar/remover **vermelho**, info **amarelo**, ações de sistema/IA **azul** (com um brilho leve). Parado, fica cinza.
- Cada ícone tem **animação própria no hover** (sino badala, engrenagem gira, etc.) e **troca animada** entre estados (encolhe + desfoca → aparece).

## Forma (aprovado em 1.4 — `design/1.4-forma.html`)
- **Tudo arredondado:** selos 6 · botões/campos 10 · linhas/balões 14 · cartões/modais 20 · janela 24 · pílula/toggle redondo total.
- **Bordas de 1 px** separam as áreas (discreta → forte em botões → azul quando ativo).
- **Profundidade:** luz fininha no topo + sombra larga (no preto, sombra comum não aparece). Hover levanta.
- **Vidro fosco só em pontos:** pílula flutuante, modal, menu suspenso e toast. Nunca em cartões ou no fundo.

## Mascote (aprovado em 1.6 — `design/1.6-mascote.html`)
- **Três mascotes**, todos nos dois azuis com olhos brilhantes: **Estrela**, **Orbe** e **Robô**.
- O usuário **alterna entre eles dentro do app** (Configurações → Personalizar, e atalho clicando no mascote do menu). A troca é animada (encolhe + desfoca → aparece).
- Hover: olhos piscam + animação própria (estrela gira, anel do orbe gira, antena do robô balança).

## Pílula flutuante (definido — será feito no Passo 7)
- **Três formatos alternáveis:** notch arredondado (grudado em cima, estilo iPhone X/11) · notch chanfrado (grudado em cima, cantos cortados em ângulo) · ilha (solta, estilo Dynamic Island).
- **Parada: preto puro, sem nenhum detalhe**, bem discreta. Detalhes (mascote, ondas, texto) só aparecem quando o Gemini é chamado, ao clicar ou quando o mouse chega perto.

## Movimento
6. **Tudo animado — nada seco.** Todo elemento tem entrada, saída, hover e mudança de estado animados (skills transitions-dev / transitions-polish).
7. **Gradientes ficam parados e só fluem com o mouse em cima** (hover). Animações de estado (ex.: pulso do microfone gravando) podem rodar sempre.
8. **Borda com gradiente girando** (tipo espiral) aparece **só no hover** e **só em um elemento por vez** na tela — ao passar para outro, o anterior apaga.
9. **Zoom no hover:** balões, botões, linhas e cartões pequenos crescem ~4% ao passar o mouse e voltam ao sair (cartões grandes ~2%). Ao clicar, afundam levemente.
10. **Ritmo (aprovado em 1.5 — `design/1.5-movimento.html`):**
    - Velocidades: instantâneo 80 · rápido 150 · normal 250 · médio 350 · lento 400 · destaque 500 ms.
    - Curvas: **suave** `cubic-bezier(0.22, 1, 0.36, 1)` (padrão) · **quique** `cubic-bezier(0.34, 1.36, 0.64, 1)` (toggle, botão, selo, destaque) · **troca** `ease-in-out` (ícone/texto) · **contínuo** `linear` (girar, brilho).
    - Hover: entra 250, sai 150 · clique: afunda 0.96 em 150 com quique.
    - Menu/modal: abre 250 (cresce 0.96→1 + desfoque) · fecha 150. Abrir sempre mais lento que fechar.
    - Painel: abre 400 (sobe 12px + desfoque 3) · fecha 350.
    - Troca de ícone/texto 150–250 (desfoca e cruza) · toggle/selo 250 quique · destaque 500 quique.
    - Cascata: 40 ms entre itens.
    - **Desempenho:** sem desfoque animado em áreas grandes (janela, página, painéis) — só opacidade + movimento; desfoque só em peças pequenas.
    - Entradas: subir (conteúdo) · crescer (menu/modal) · deslizar (troca de aba) · saltar (check/destaque) · tremer (erro).

## Processo
11. Um subpasso do `ROADMAP.md` por vez; mostrar, esperar aprovação, marcar `[x]`.

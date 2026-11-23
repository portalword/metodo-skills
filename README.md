# metodo-skills

**Plan first. One step at a time. A design system that stays consistent.**

Two AI agent skills that turn any coding AI (Claude Code, Codex, Cursor, DeepSeek Harness…) into a disciplined project
partner: it plans the whole project before writing code, builds it one approved step at a time, keeps a live checklist you
can tick and comment on, and designs the interface from a written rule book instead of guessing.

Created by **José** — Instagram [@jxj.jose.jxj](https://www.instagram.com/jxj.jose.jxj) — together with
[Claude](https://claude.ai) (Anthropic). Born while building a full desktop AI assistant in a few days.

> The skills' instructions are written in **Portuguese (pt-BR)**; any modern AI reads them fine and answers in your language.

---

## What's inside

| Skill | What it does |
|---|---|
| **metodo-projeto** (project method) | **Plan lock**: no code until the full `ROADMAP.md` is approved. Steps and sub-steps, one at a time; "approved" = tick + commit + next. Live checklist, `PLANOS-FUTUROS.md` (future ideas), "really done" checklist, no silent errors, security rules, git backups, performance checks. |
| **design-sistema** (design system) | HTML samples → you choose → rules written in `design/REGRAS.md` → components → screens → visual review. Universal principles (no explanatory text, color only with meaning, concentric corners, calm when idle, accessibility) plus a default style each project can override. |

The two work as a pair: each one knows which rules belong to the other, and there is a clear priority order
(your request → project files → these skills → third-party skills → AI defaults), so rules never fight each other.

## Live checklist

Your `ROADMAP.md` becomes a page in a side tab (`http://127.0.0.1:8765`) that both you and the AI use:

- ✔ done · **–** half-done (yellow) · ☐ to do — click to cycle; the page opens on the **current** item.
- Comment on any item; the AI answers right below it.
- Tabs: **All · To do · Done · Design** (palette, fonts and corners drawn from `design/REGRAS.md`) **· Future** (ideas for later).
- Light and dark mode.
- Runs on plain Python (standard library only) and listens only on `127.0.0.1`.

## Subagents

| Agent | What it does |
|---|---|
| **Visual critic** | Sees only screenshots, the contract and the design rules. Any defect = rejected. |
| **Tester** (`testador`) | Gets only the project folder and the step. Uses the program in a copy, tries to break it and answers with proof. No excuses: the developer can only fix. |

The **Subagents** tab sets on/off, round limit, model, self-approval, delivery test, and "approve everything without tests"
(recorded as *approved without testing*).

## Chat commands

Every time the checklist opens (or when the AI can't open a browser) it sends this list — nothing else:

| Command | Shows / does |
|---|---|
| `/abrir-checklist` · `/open-checklist` | open the checklist page |
| `/checklist` | everything |
| `/falta` · `/todo` | what's left |
| `/feitos` · `/done` | what's done |
| `/atual` · `/current` | where we stopped |
| `/design` | visual rules |
| `/futuro` · `/future` | ideas for later |
| `/comentarios` · `/comments` | questions and answers |
| `/marcar` `/metade` `/desmarcar 1.2` · `/check` `/half` `/uncheck 1.2` | mark done · half-done · not done |
| `/comentar` · `/comment 1.2 text` | comment on an item |

In **Claude Code** they are real slash commands. In other tools, type them in the chat; the AI runs
`kit/checklist/texto.py` and shows the result.

## Install

**Easiest:** tell your AI *"install metodo-skills from https://github.com/portalword/metodo-skills"*.

**Manual:**

```powershell
# Windows
git clone https://github.com/portalword/metodo-skills
powershell -ExecutionPolicy Bypass -File metodo-skills\install.ps1
```

```sh
# macOS / Linux
git clone https://github.com/portalword/metodo-skills
sh metodo-skills/install.sh
```

The installer copies both skills and the chat commands into `~/.claude` (pass another folder for other tools), then asks
before downloading the third-party skills from their **official** sources.

### Third-party skills (not included — installed from their authors)

| Skill | Used for | Source |
|---|---|---|
| design-taste-frontend | websites and landing pages | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| interface-design | apps, dashboards, settings, tables | [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) |
| transitions-dev / transitions-polish | animations and motion timing | [transitions.dev](https://transitions.dev) (manual download, see their terms) |
| dataviz | charts and KPIs | built into some AI tools; skipped if missing |

They belong to their authors and are **not** redistributed here. `design-sistema` works without them and offers to install
any that are missing.

## How a project goes

1. *"Let's build an app that…"* → the AI asks questions and writes `ROADMAP.md`. **No code yet.**
2. You review it in the checklist tab, comment, and say **"approved"** → `Plano aprovado em …` is written at the top; code is unlocked.
3. With an interface: color/font/shape samples → you pick → `design/REGRAS.md`.
4. One sub-step at a time. Each "approved" ticks the item, commits, and starts the next one.
5. When a step closes, the AI reviews earlier steps for anything left `[ ]` or `[-]`.
6. Ideas for later go to `PLANOS-FUTUROS.md`, never straight into code.

## License

© José ([@jxj.jose.jxj](https://www.instagram.com/jxj.jose.jxj)). Free to **use** in your own projects, personal or
commercial. **Not allowed:** republishing, selling, or redistributing these skills (modified or not) as your own.
See [LICENSE](LICENSE).

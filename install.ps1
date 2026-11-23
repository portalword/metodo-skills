# metodo-skills installer (Windows / PowerShell)
# Usage:  powershell -ExecutionPolicy Bypass -File install.ps1  [-Target "$HOME\.claude"]  [-NoThirdParty]
param(
  [string]$Target = "$HOME\.claude",
  [switch]$NoThirdParty
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$skills = Join-Path $Target "skills"
$commands = Join-Path $Target "commands"
$agents = Join-Path $Target "agents"
New-Item -ItemType Directory -Force $skills, $commands, $agents | Out-Null

Write-Host "Installing metodo-projeto and design-sistema into $skills"
Copy-Item -Recurse -Force (Join-Path $here "skills\metodo-projeto") $skills
Copy-Item -Recurse -Force (Join-Path $here "skills\design-sistema") $skills
Write-Host "Installing chat commands into $commands"
Copy-Item -Force (Join-Path $here "commands\*.md") $commands
Write-Host "Installing the testador agent into $agents"
Copy-Item -Force (Join-Path $here "agents\*.md") $agents

if ($NoThirdParty) { Write-Host "Done (third-party skills skipped)."; exit 0 }

# Third-party skills are NOT bundled (their licenses). They are downloaded from their official sources.
Write-Host ""
Write-Host "Third-party skills (downloaded from their official sources):"
Write-Host "  design-taste-frontend  https://github.com/Leonxlnx/taste-skill"
Write-Host "  interface-design       https://github.com/Dammyjay93/interface-design"
Write-Host "  transitions-dev/polish https://transitions.dev  (manual download, see their terms)"
$ok = Read-Host "Download the first two now? (y/n)"
if ($ok -notmatch '^[yYsS]') { Write-Host "Skipped. The skills still work without them."; exit 0 }
if (-not (Get-Command npx -ErrorAction SilentlyContinue)) {
  Write-Host "npx (Node.js) not found. Install Node.js, or install them manually from the links above."; exit 0
}
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
npx skills add https://github.com/Dammyjay93/interface-design --skill interface-design
Write-Host ""
Write-Host "Done. transitions-dev / transitions-polish: get them at https://transitions.dev"

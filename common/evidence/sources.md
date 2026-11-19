# Sources

Which repos and eras back which rule families. Paraphrased; repo names appear where they help to re-check the evidence.

## Backing by Family

| Family | Main sources | Era | Notes |
| --- | --- | --- | --- |
| PRIN | all of the below | 2021-2026 | stated rules from the owner |
| GO, PULUMI | shared-library, github-infrastructure, vault, mail-services, home-cluster infrastructure, adguard provider; secondary: game-director, watermeter, assignment-infrastructure (grep) | 2023-2026 | strict config from 2025; 2023 adguard is built on a template |
| PY | onyx-client, onyx-homeassistant-integration, node-red backup_restore; toolkit ruff config (Tier 1.5) | 2021-2026 | human baseline 2021-2025 |
| SH | vault and mail-services assets, HA lifecycle scripts, applications scripts | 2023-2026 | docblocks and banners are AI-era |
| K8S | home-cluster applications, infrastructure, k8s-demos, HA configuration, container and DNS repos | 2023-2026 | 2026-09 sweeps untrailered, weight 0.5 |
| YAML | cluster app values, infrastructure repos, mealie, Home Assistant configuration | 2023-2026 | 829 of 831 files start with `---`; yamllint in 4 of 5 spot-checked repos |
| CONF | pgvecto and node-red container repos, DNS repo, Home Assistant configuration tree | 2023-2026 | one repo family each, skimmed only |
| MAKE | 11 Go Makefiles | 2022-2026 | new Makefile shape stated |
| CI, RENOV, MISE | applications, github-infrastructure, vault, HA, container repos, renovate-config | 2023-2026 | mise migration 2026-10-25: 21 of 29 commits trailered (0.75), the rest 0.5 |
| NIX | homelab-router-infrastructure, dev-infrastructure | 2026 | 22 of 25 router commits untrailered, weight 0.5; no written rules in the repos |
| TYPST | a Typst document repo | 2026 | one repo |
| DOC, README, RB | 20 READMEs, docs commits, working notes (Tier 1.5) | 2021-2026 | untrailered 2026 text weight 0.5 |
| COMMIT | 5216 commits in 40 repos; 37 conform configs | 2021-2026 | all years |
| PR | the owner's PRs, issues and issue comments in onyx, adguard, proxmox provider, third-party repos | 2021-2026 | no review comments exist |
| MAIL | sent mail, about 95 analyzed | 2024-2026 | abstract only |

## Excluded as Evidence

| Repo or material | Reason |
| --- | --- |
| telegraf-output-kinesis-data-firehose | excluded by the owner |
| pulumi-proxmoxve | excluded for code style; used only for reply and PR text |
| dotfiles, esphome (code), documentation, recording-transcriber (prose) | excluded or WIP; recording-transcriber seen only for lint-task shape, low weight |
| teaching documents and teaching-toolkit | AI-generated; used as Tier 1.5 (weight 0.5, caps at `lean`) for rules the owner wrote into docs, never for code or prose style |
| adguard webhook skeleton | upstream template; only the owner's behavior code counted |
| generated files (release-please changelogs, lockfiles, `gotk-components.yaml`) | generated boilerplate |
| deprecated repos (public-services, shared-services, node-red-container) | commit style only |
| bot commits (Renovate, GitHub Actions, Dependabot) | not the owner's |
| 2026 AI-heavy docs (restore.md, BOOTSTRAP.md, vault BGP sections) | weight 0.5 and capped at `prefer` (confirmed by the owner 2026-11-18) |

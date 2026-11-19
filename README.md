# Style Guide

[![License](https://img.shields.io/github/license/muhlba91/style-guide?style=for-the-badge)](LICENSE.md)
[![Build status](https://img.shields.io/github/actions/workflow/status/muhlba91/style-guide/verify.yml?style=for-the-badge)](https://github.com/muhlba91/style-guide/actions/workflows/verify.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/muhlba91/style-guide/badge?style=for-the-badge)](https://scorecard.dev/viewer/?uri=github.com/muhlba91/style-guide)

This repository contains the owner's coding, documentation and writing style as rules with evidence, and skills that let agents write in the style, review against it, and keep it current.

---

## Requirements

- [mise](https://mise.jdx.dev)

## Layout

| Path | Content |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md` | Working rules for agents. `CLAUDE.md` links to `AGENTS.md`. |
| `common/principles/` | Rules across languages and artifacts. |
| `common/languages/` | Deltas per language or file type. |
| `common/writing/` | README, runbook, prose, commit, PR and issue text, email. |
| `common/evidence/` | Method, weighting and sources behind the rules. |
| `common/digest/` | Generated lean digests of the rules, read by the write and review skills (`make digest`). |
| `common/skills/` | The skills `style-write`, `style-review`, `style-update`, `style-audit`. |
| `.agents/skills/`, `.claude/skills` | Relative links to every skill (`make skills`). |
| `OPEN-QUESTIONS.md` | Decisions still open. |
| `CHANGELOG.md` | One line per rule change. |
| `common/retired.txt` | Retired rule IDs, never reused. |
| `mise.toml`, `mise.lock`, `.pre-commit-config.yaml`, `.conform.yaml`, `.markdownlint.yaml`, `.yamllint.yml` | Pinned tools, hooks and linter configs. |
| `.github/`, `renovate.json` | CI workflows and Renovate. |
| `scripts/`, `tests/`, `Makefile` | Quality gate (`make check`) and installer. |
| `LICENSE.md` | AGPL-3.0. |
| `llms.txt` | Machine-readable index. |
| `work/` | Gitignored scratch and audit reports. |

## Rules

Rule format, strength and status: see `AGENTS.md`. The rules cover Go, Pulumi, Python, shell, Kubernetes YAML, GitHub Actions, Renovate, mise, Nix, Typst, Makefiles, container, DNS and Home Assistant configuration, READMEs, runbooks, docs, commit messages, PR and issue text and email. This is a personal style guide: fork it and make it yours by changing the rules.

To change a rule, ask `style-update`, or edit the rule file, run `make digest` and `make check`, and add a line to `CHANGELOG.md`. Never reuse a retired ID.

## Skills

| Skill | Use |
| --- | --- |
| `style-write` | Write or edit code, docs, commits, PR text or email in the style. |
| `style-review` | Review a change against the rules and report findings with rule IDs. |
| `style-update` | Change the rules from feedback or new evidence, after the owner approves. |
| `style-audit` | Audit the guide itself and test it on held-out work. |

The loop: write, review, collect the owner's corrections, update, audit.

### Install

```bash
make install
```

This links every skill into `~/.claude/skills` and `~/.agents/skills` and needs only bash. Set `STYLE_GUIDE_SKILL_DIRS` (space separated) to use other folders. A link that points elsewhere is left alone and reported.

The links point into this checkout. Keep it in place and run `make install` again after moving it. Do not copy the skill folders: a skill finds the guide by walking up from its link to `AGENTS.md` and stops with an error when there is none. Update with `git pull`, uninstall by removing the `style-*` links.

### Use

Name the skill in the prompt:

```text
/style-write add a retry option and commit it
/style-review
/style-update this finding is wrong, the rule should say X
/style-audit
```

- Agents without slash commands: ask for the skill by name, or link the skills into the folder that agent reads (`STYLE_GUIDE_SKILL_DIRS`) and point it at `AGENTS.md`.
- The skills also trigger from their descriptions. That is not guaranteed and was not tested with installed skills.
- A subagent does not inherit installed skills: give it the absolute path of `common/skills/style-write/SKILL.md` in this checkout.
- Order of precedence: the task instruction, then the target repository's own rules, then this guide.
- Optional global instruction for `~/.claude/CLAUDE.md` or the agent's global file. It costs about 100 tokens per session, loads the skill only for substantial writing and is untested as a trigger. The commit line works even when the skill does not load (COMMIT-17). Without it, call the skills by hand.

```text
Use the style-write skill before writing docs, PR text or an email, creating a file, or adding a new function or resource; skip it for questions and small edits that follow the surrounding code.
Commits: Conventional Commits, lowercase imperative, 3 to 6 words (100 characters at most), no prose body, scopes only ci, deps and release (never as a type), and no attribution (no Co-Authored-By, no Signed-off-by, no "Generated with").
```

### Model Choice

Result of the first evaluation (2026-11, one to two runs per case, summary in `common/evidence/README.md`):

| Work | Model class |
| --- | --- |
| New repositories, multi-file changes, anything without a template next to it | Sonnet |
| Small, well-scoped changes next to existing files, followed by a `style-review` pass | Haiku, at about a tenth of the cost |
| Reviewing a small change with `style-review` | Haiku: it caught a planted violation and stayed quiet on clean changes, but may add a suggestion your own practice contradicts |
| Full audit with `style-audit` | A stronger model than the one that changed the rules |
| Any writing without the skill | Avoid: every such run added the forbidden attribution trailer, and designs differed where no template was nearby |

Haiku with the skill came close to Sonnet on small changes. On whole new repositories its runs varied more and one missed a file the program needs, so review those.

### Token Load

- `style-write` is small (a few hundred tokens), `core.md` about two thousand, each digest a few hundred to under two thousand. A task loads a few thousand tokens of the guide, never the full rules.
- Installed skills add their descriptions to every session (a couple of hundred tokens in total).
- In the evaluation, a skilled run used about the same to 30 percent more tokens than an unskilled one. A `style-review` pass of a small change cost about as much again.

---

## Continuous Integration and Automations

- GitHub Actions: conform on commit messages, lint, and the rule, digest and test checks (`.github/workflows/verify.yml`), plus dependency review, CodeQL and OpenSSF Scorecard.
- Renovate Bot: keeps actions, pre-commit hooks and mise tools current (`renovate.json`).

## Development

Tool versions (mise, Python, Node, shellcheck, yamllint, markdownlint) are managed with mise: run `mise trust` and `mise install` once, then use `make check` for the gates of CI (conform runs on commit messages instead), `make digest` after a rule change and `make help` for the rest.

Without mise, put python3, shellcheck, yamllint and markdownlint-cli2 on the PATH.

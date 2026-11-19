# README

Evidence: 14 service, IaC and config READMEs sharing one skeleton since 2023 (github-infrastructure `068015f` onward), library READMEs (onyx, adguard, docker_helm) with a variant. Weight 1.0 for 2023 origin, 0.75 for trailered 2026 edits, 0.5 for untrailered ones.

## README-01 · must · common · stated

- Rule: Build every repo README to one skeleton, in the order given under Good; library and client READMEs use README-10's middle; other deviations are decided per repo and noted in that repo.
- Why: 11 of 14 service repos share it; libraries and clients use another middle (Installation, Usage, Configuration, Development), which is a per-repo exception.
- Good: H1, badge row, one-sentence intro (`This repository contains the infrastructure as code (IaC) for X using Pulumi.`), `---`, Requirements, Creating, Destroying, Environment Variables or Secrets, `---`, Configuration (one H3 per block), `---`, Continuous Integration and Automations, Development.
- Bad: a marketing paragraph before the purpose.
- Source: stated 2026-11-18, README skeleton. Evidence: github-infrastructure, mail-services, vault, home-cluster, esphome, ring-mqtt, HA configuration, renovate-config, gitstream-config, agents/configuration.
- Check: judgment

## README-02 · prefer · common · observed

- Rule: Title homelab repos `Homelab: <Area> - <Part>` and other repos with the plain product name; add no tagline.
- Why: 7 of 14 repos; the homelab title is a per-repo exception to a plain name (README-01).
- Source: no owner statement on titles; the per-repo exception follows the stated skeleton decision (README-01). Evidence: applications, infrastructure, esphome, HA configuration, agents; vault `muehlbachler: Core Infrastructure`.
- Check: judgment

## README-03 · must · common · stated

- Rule: Put a row of `style=for-the-badge` badges directly under the H1, followed by a blank line and the intro: shields.io badges, except the OpenSSF Scorecard badge, which comes from `api.scorecard.dev`; a support button such as Buy Me a Coffee may sit in the row.
- Good: H1, then the `for-the-badge` row (shields.io badges plus the Scorecard badge from `api.scorecard.dev`), a blank line, then the intro.
- Bad: badges after the intro, or default-style badges.
- Source: stated 2026-11-19, Scorecard badge from `api.scorecard.dev`. Evidence: all 20 READMEs read; typical badges are build status, license, OpenSSF Scorecard, coverage, release date, PyPI, in varying order; scorecard badge in one sweep 2024-10-27. Alt text is often empty.
- Check: judgment

## README-04 · prefer · common · observed

- Rule: In IaC READMEs, separate major blocks with `---` on its own line, not between every H2; library and client READMEs may use `---` before Development and Contributors.
- Source: IaC READMEs; inconsistent inside blocks; library READMEs use none after the intro.
- Check: judgment

## README-05 · must · common · stated

- Rule: In Requirements, name and link mise in one line and nothing else. Open the Development section with one sentence: tool versions (list them) are managed with mise, without a second link; run `mise trust` and `mise install` once, then use the usual commands (list them).
- Why: `must` rests on the owner naming mise as a standard; the repo evidence is one sweep, treated as one source at reduced weight.
- Good: Requirements has `- [mise](https://mise.jdx.dev)`; Development opens with `Tool versions (Go, golangci-lint, Pulumi) are managed with mise: run \`mise trust\` and \`mise install\` once, then use \`make lint\`.`
- Bad: per-tool download links in Requirements.
- Source: stated 2026-11-19, mise linked once in Requirements and not again in Development. Evidence: 31 repos have `mise.toml` and `mise.lock`; 29 migration commits on 2026-10-25, 21 with AI trailers (0.75) and 8 without (0.5); `ccb494b` collapsed a 3-item list into one line.
- Check: judgment

## README-06 · must · common · observed

- Rule: End IaC and config READMEs with "Continuous Integration and Automations" (two bullets, GitHub Actions and Renovate Bot), then Development.
- Good: a section "Continuous Integration and Automations", followed by Development, with `- GitHub Actions: lint and deploy on push` and `- Renovate Bot: updates images and actions`.
- Bad: CI details scattered through the README with no closing section.
- Source: 10 repos, text identical since 2023; CV extended it with what typstyle enforces.
- Check: judgment

## README-07 · must · common · observed

- Rule: In IaC and config READMEs, document each configuration key in a `yaml` block whose values are the descriptions, mirroring the structure, one H3 per top-level key, with no table; suffix `(optional, default: X)` and `(e.g. ...)` in that order, and put units in the description (`in s`, `in ms`, `in %`).
- Why: the suffixes mark each key at a glance; library READMEs use a table (README-10).
- Good: `### vault` over `address: the vault url (e.g. https://vault.example.org)` and `timeout: request timeout in s (optional, default: 30)`.
- Bad: a Markdown table of keys and descriptions.
- Source: mail-services, vault, github-infrastructure, infrastructure; 2023 initial commit, extended 2026 by the owner in the same form; the unit and default suffixes also in the onyx-homeassistant-integration table (2023-2026).
- Check: judgment

## README-08 · must · common · observed

- Rule: List environment variables as `- \`NAME\`: the lowercase description`, grouped by provider, not in a table.
- Good: ``- `API_TOKEN`: the api token of the provider``.
- Bad: a table with columns Name and Description.
- Source: all Pulumi repos since 2023; `29f4850` fixed a missing colon (human).
- Check: judgment

## README-09 · prefer · common · observed

- Rule: In IaC READMEs, open a Configuration section that holds secrets with a bold-italic `***Attention:***` line pointing to the tool's secret encryption; library READMEs may use plain `**Attention**:`.
- Source: github-infrastructure, mail-services, vault, identical since 2023.
- Check: judgment

## README-10 · prefer · common · observed

- Rule: Library and client READMEs replace README-01's middle with Installation, Configuration (a table with Option and Description), Usage and Development, in that order; a library without options has no Configuration section; README-07's no-table rule does not apply to them.
- Source: onyx-client, onyx-homeassistant-integration, adguard, docker_helm.
- Check: judgment

## README-11 · prefer · common · stated

- Rule: Add Contributors and Supporting sections (including generated all-contributors blocks and support text) only to published open-source projects, never to private repos.
- Why: present in onyx, adguard, watermeter and docker_helm, absent in private repos.
- Source: stated 2026-11-18, Contributors and Supporting sections. Evidence: 4 public repos; the private repos checked show none, which is absence, not a rule.
- Check: judgment

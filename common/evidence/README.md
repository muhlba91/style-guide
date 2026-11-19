# Evidence

How the rules were derived. No rule depends on reading the source repos.

## Method

Seven domain passes read the owner's material read-only (Go, Python, config and shell, prose, commits and PRs, Nix, email). The source classes are public repos, some private repos, private working notes, and private mail as abstract features only (no content is kept). Each pass produced rule candidates with evidence, counter-evidence and open questions. The rules here merge those passes. Nothing was invented: a rule needs concrete observed evidence or an owner statement.

## Weighting

- 1.0: the owner's commits and text without AI trailers that read as the owner's own.
- 0.75: Tier 1 commits with an AI trailer that the owner reviewed. Stated by the owner on 2026-11-18: they weigh "a bit less" than the owner's own commits. They are not capped at `prefer`.
- 0.5: untrailered text from 2026 that reads as AI-written (long clause chains, em dashes, wrapping at 100 to 120, banners, `Args:` docblocks). It shows what the owner accepted, not what the owner writes. It alone never raises a rule and caps at `prefer`. This covers the untrailered sweeps `e093196d` and `4cf96084`, 22 of 25 router Nix commits and the untrailered part of the 2026-10-25 mise sweep; a commit with a trailer weighs 0.75.
- 0.5, Tier 1.5: files the owner influenced but an AI built wholly (teaching-toolkit, working plans). They never raise a rule alone and cap at `lean`.
- The human and AI split is unreliable for 2026: untrailered work is often AI-shaped too. Trailers are the only mechanical signal for older work. From 2026-11-18 the owner's standard is no attribution (COMMIT-17), so newer AI-assisted commits carry no trailer: judge them by shape, at weight 0.5, until the owner says which are the owner's own wording.
- Older history is preferred when a repo shows heavy recent AI use. The human baseline is 2021 to 2025.
- Edits the owner made over AI text are the strongest taste signal; few exist (an AI comment turned into a why, stale lists removed, wrapped paragraphs rejoined).
- Stability: a pattern seen in many repos and years beats one seen once.

## Tiers

| Tier | Meaning | Maximum strength |
| --- | --- | --- |
| Stated | the owner said it in this project | `must`, status `stated` |
| 1 | the owner's repos, human baseline across repos and years; AI-trailered commits the owner reviewed count at 0.75 | `must` |
| 1.5 | files the owner influenced but an AI built wholly (teaching-toolkit, working plans), weight 0.5 | `lean`; never the only basis |
| 2 | untrailered AI-shaped text the owner kept after review, weight 0.5 | `prefer` at most, `lean` if single source |
| Email | sent mail 2024-2026 | `lean`, abstract features only |

## Stated Evidence

Owner statements are recorded as `stated` with the date and topic. The weighting statement above (2026-11-18, AI-trailered commits weigh a bit less) is one of them. "Common first, language deltas" is stated too (see the layout in `AGENTS.md`). The statements of 2026-11-19 from the first evaluation (manifest bundling, Gatus and certificate handling, workflow permissions, optional Pulumi config, commit scopes versus types, shared per-site values, badges, mise links, copyable text) are listed in `CHANGELOG.md`. Reference projects (stated 2026-11-18): shared-library and the onyx projects (onyx-client, onyx-homeassistant-integration) are the work the owner values most; where repos conflict, their conventions win, but their legacy patterns do not bind new code. New code follows this guide and general best practices, not legacy habits (stated 2026-11-18). shared-library favors simplicity, for example no unneeded nil checks. Quality and effectiveness win over token savings when they conflict (stated 2026-11-18). Adopted tool configs (the shared golangci-lint config is the upstream template, release-please and Home Assistant defaults) count as tool choices the owner made, not as the owner's authorship (stated 2026-11-18). Confirmed 2026-11-18: untrailered 2026 text that reads as AI-written weighs 0.5 and caps at `prefer` until the owner says which parts are the owner's own wording.

## Status

- `stated`: owner statements override contrary evidence.
- `observed`: derived from evidence.
- `open`: evidence is split or the owner must decide. The better-supported default is written in the rule and the question is in `../../OPEN-QUESTIONS.md`.

## Skill Evaluation

First test of `style-write` and `style-review`, 2026-11, with fresh agents of two model classes (Sonnet and Haiku), with and without the skill:

- Method: replays of two real changes from the owner's repositories (starting from the parent commit, no history of the result) and one new repository. Outputs were compared with the real change, built, linted, and reviewed blind with `style-review` by a separate agent.
- Cost: a skilled run used about the same to roughly 30 percent more tokens than an unskilled one, and a `style-review` pass of a small change cost about as much again. Haiku used more tokens per task than Sonnet at about a tenth of the price. To repeat the test, use `style-audit`.
- Without the skill, every run added the forbidden attribution trailer, built a different design where no template was nearby, and had 18 `must` violations against 4 for the skilled Sonnet run on a whole repository (one run each).
- With the skill, small changes matched the real change closely. Haiku was close to Sonnet on small changes at a tenth of the cost, and less reliable on a whole repository: one run missed a file the program needs, which its own checks could not catch.
- Reviews of small changes by Haiku matched Sonnet on clean changes, caught a planted attribution trailer, and added one `prefer` suggestion that the owner's own commit contradicts. Whole-repository reviews were run by Sonnet only.
- Findings fed back into the rules: bundled manifests as an exception to file naming, Gatus and certificate handling, top-level workflow permissions, optional Pulumi config, commit scopes versus types, a new-repository file checklist, and no third-party names in rules.
- A review of a clean output returned nothing, which shows the output matches the guide, not that the guide matches the owner's habits. Reject wrong findings through `style-update`.
- Limits: one to two runs per cell. Shell, Python, Nix, Typst, email, runbooks and PR text were reviewed but not write-tested, and the skills were read by path, not triggered as installed skills.

## Mechanical Versus Judgment

`Check: tool:<name>` appears only where a configured tool in the owner's repos enforces the rule. `scripts/check_rules.py` keeps the allowed names in `ALLOWED_TOOLS`. Where a tool only helps (renovate for pins, mise for versions), the Check says `judgment` and names the tool. shellcheck runs in 10 or more repos. markdownlint is configured in 5 repos, 3 of them evidence-eligible. A config that exists only in AI-built teaching material (strict `ruff.toml`) is not claimed as the owner's standard.

## Excluded and Limits

See [`sources.md`](sources.md). Known gaps: no data before 2021; email only 2024 to 2026; no PR review comments by the owner exist; evidence for 2026 services is heavily AI-assisted even without trailers; the Nix repos hold no written rules, only code.

## Privacy

Rules paraphrase. No verbatim private text, email content, names, amounts or secrets are stored here.

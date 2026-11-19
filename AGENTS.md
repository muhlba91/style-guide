# Style Guide (Read Me First)

The owner's coding, documentation and writing style as rules with evidence, plus skills to write in the style, review against it, and keep the guide current. Tool-neutral: any agent can read the Markdown directly.

## Layout

- `common/principles/`: rules that hold across languages and artifacts.
- `common/languages/`: deltas per language or file type. A rule that holds in several languages lives once in the principles.
- `common/writing/`: README, runbook, prose, commit, PR and issue text, email.
- `common/evidence/`: method, weighting and provenance. No rule depends on reading the source repos.
- `common/digest/`: generated lean views of the rules for `style-write` and `style-review` (`make digest`). Edit the rule files, never the digests.
- `common/skills/`: `style-write`, `style-review`, `style-update`, `style-audit`. `.agents/skills/` and `.claude/skills` link to them (`make skills`).
- `common/retired.txt`: retired rule IDs, never reused.
- `OPEN-QUESTIONS.md`: decisions the owner has not made. Rules with status `open` point to an entry.
- `.github/`, `renovate.json`: CI (conform, lint, rules, digests, tests, dependency review, CodeQL, Scorecard) and Renovate. `make check` runs the same gates locally, except conform, which pre-commit runs on the commit message.
- `work/`: gitignored scratch and audit reports. Never commit it.

## Rule Format

```markdown
## GO-26 · must · go · observed

- Rule: one imperative sentence.
- Why: one line.
- Good: tiny example. Bad: tiny counter-example.
- Source: paraphrased evidence, repos, era, frequency.
- Check: judgment, or tool:<name> (only a configured tool that enforces the rule)
```

A rule must not be both `must` and `open`; use `prefer` with `open`. A `stated` rule has Source `stated YYYY-MM-DD, <topic>`. A rule file has one H1 and one H2 per rule (plus optional sections such as Avoid), with a blank line below the header. The ID is `<FAMILY>-<NN>` with two digits. Strength: `must` (stated or consistent), `prefer` (usual), `lean` (tendency, single source). Status: `stated` (the owner said it), `observed` (evidence), `open` (undecided, see `OPEN-QUESTIONS.md`).

## Precedence

- First, the user's instruction in the task.
- Then the target repository's own rules (`AGENTS.md`, `CLAUDE.md`, linter and formatter configs). Surrounding code decides only where this guide is silent: new code follows the guide, not legacy habits.
- Last, this guide: `must`, then `prefer`. Apply `lean` only when nothing above speaks to the point. Where repos conflict, the reference projects (shared-library, onyx) win.

A tool's default attribution never beats COMMIT-17 and PR-18. Quality wins over token savings: read the full rule when a digest rule is unclear.

## Working Rules

- Use `style-update` to change a rule. The owner approves every change before it is applied.
- Raise a strength only with an owner statement or two independent sources. Tier 1 commits with AI trailers that the owner reviewed weigh 0.75 (stated: "a bit less" than the owner's own) and are not capped. Untrailered text that reads as AI-written weighs 0.5, caps at `prefer` (`lean` if it is the only source) and never raises a rule alone. Tier 1.5 material weighs 0.5 and caps at `lean`.
- Keep skills and digests lean, but grow them where review shows they lose accuracy.
- Put every scope, exception and precedence of a rule in its Rule sentence: digests drop Why and Source.
- Name a third party's annotation key or field in a rule only when the owner requires it and a review would miss it; name no API versions.
- The guide follows its own style: crisp, precise, grounded, no filler, no em dashes, no emoji.
- Write "the owner", never a gendered pronoun (the checker enforces it).
- Paraphrase evidence. No personal data, secrets, email details or private content in this repository.
- Run `make check` when a change is finished, not after every edit (`mise exec -- make check` when the pinned tools are not on PATH). A large change is more than 10 rules changed, a new family or a restructure: then run `style-audit` in full mode with a stronger model than the author, then the owner reviews.
- Commit and push only when asked. Commits are Conventional Commits, lowercase, imperative, without a trailing period (`.conform.yaml`).

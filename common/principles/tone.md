# Tone and Surface Style

## PRIN-08 · must · common · stated

- Rule: Keep the tone grounded; no exaggeration, hype or superlatives; a plain factual statement or feature list is not hype.
- Why: stated.
- Good: `This should fix the timeout.`
- Bad: `This completely eliminates all timeout problems!`
- Source: stated 2026-11-18, tone. Evidence: human replies use `should fix`, `hopefully`, `might be`; AI-written README text ("integrates seamlessly") is the counter-example.
- Check: judgment

## PRIN-09 · must · common · stated

- Rule: Write in English by default, for code, comments, docs, commits and issues.
- Why: stated; recipients and public repos.
- Good: `// retry once if the socket is closed` and a commit `fix: handle empty response`.
- Bad: a German comment or commit subject in a public repo.
- Source: stated 2026-11-18, English by default. Evidence: Email is out of scope (see MAIL rules).
- Check: judgment

## PRIN-10 · must · common · observed

- Rule: Write impersonal, present-tense, declarative prose; address the reader as "you" only in direct instructions; no marketing wording (superlatives and hype adjectives such as "powerful", "seamless"); a factual feature list is fine.
- Good: `The stack is deployed via pulumi up.`
- Bad: `You will love how seamlessly the powerful stack deploys.`
- Source: all human READMEs 2021-2025 (17 of 17); counter-example is AI text in watermeter.
- Check: judgment

## PRIN-11 · must · common · observed

- Rule: Do not use em dashes; use a colon, comma, semicolon or parentheses; use `->` only in commands.
- Why: strongest authorship fingerprint.
- Good: `v6-only features are unavailable; their calls fail.`
- Bad: the same sentence with an em dash between the clauses.
- Source: 0 em dashes in 8 human README sets and about 95 emails; 13 to 20 per file in AI-assisted docs (applications, teaching documents), 2026.
- Check: judgment (a grep for the character works)

## PRIN-12 · must · common · stated

- Rule: Do not use emoji in code, comments, docs, headings, commit subjects, PR titles, replies or script output; generated content such as an all-contributors table is exempt.
- Why: no emoji in 17 of 17 hand-edited READMEs; fluff. About one reply in three to strangers ended with a thumbs up or smile; that is not the standard.
- Good: `done: 3 created, 1 skipped`.
- Bad: a check-mark symbol prefix on status lines.
- Source: stated 2026-11-18, emoji in replies. Evidence: only AI-era exceptions (vault info callout, KRR report bullets, shell validator output), 2026.
- Check: judgment

## PRIN-13 · must · common · observed

- Rule: Do not decorate: no banners, box-drawing lines, ASCII art frames or all-caps emphasis in output, comments or docs.
- Good: `### docker ###` as a plain section label in provisioning scripts.
- Bad: a framed multi-line header made of drawing characters.
- Source: box-drawing banners appear only in AI-era shell scripts (applications `validate-manifests.sh`, HA `util.sh`, 2026); the owner's own scripts use short labels.
- Check: judgment

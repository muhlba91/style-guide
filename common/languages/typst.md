# Typst

Evidence: curriculum-vitae only (one human edit `1ba2f15`, 2026-10; CI `58eeb98`, 2026-08). One repo, so no rule is above `prefer`. Deltas against `../principles/` and `../writing/prose.md`.

## TYPST-01 · prefer · typst · observed

- Rule: Format with `typstyle --wrap-text=sentence --line-width 160` locally and in CI; build through a script that downloads fonts into a git-ignored `fonts/`.
- Source: CV README and workflow; the only line-width rule in the owner's repos.
- Check: tool:typstyle

## TYPST-02 · lean · typst · observed

- Rule: Write CV bullets one achievement per bullet, verb first, with concrete scope (customers, team size, technology), semicolon-chained clauses, no first person and no self-praise.
- Good: `Led a five-person team through a platform migration; introduced code review and automated deploys.`
- Bad: `Was responsible for various tasks around servers.`
- Source: `1ba2f15` rewrote vague bullets into specific ones (human).
- Check: judgment

## TYPST-03 · lean · typst · observed

- Rule: Write dates as `MM/YYYY - MM/YYYY`, the title line as `Role · Role · Role`, and contact items separated by `|`; extract repeated markup into named helpers (`contact-item`, `contact-sep`).
- Source: `1ba2f15`.
- Check: judgment

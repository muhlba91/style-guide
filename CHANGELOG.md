# Changelog

One line per change to the rules: date, rule ID, what changed. Written by `style-update`. Retired IDs are in `common/retired.txt`.

## 2026-11-23

- PRIN-42: lint with the linters that make sense for the repo; a file type alone does not justify one.
- PRIN-50: yamllint is the exception to pinning linters in `mise.toml`; it comes from a local install (its mise build breaks Python 3.15 repos).
- YAML-04: yamllint only where hand-written YAML is a main artifact, from a local install.
- CI-11 (new): actionlint in every repo with workflows, as a pre-commit hook and a required PR job. CI-04 gate list and CI-09 example follow.
- Guide repo: yamllint removed (mise, `.yamllint.yml`, `lint-yaml`), actionlint added (mise, pre-commit hook, `verify.yml` job). YAML-01 and YAML-03 checks are judgment.
- New Repository Checklist: linter configs only where the linter fits; actionlint for workflows.

## 2026-11-19

- CI-01: when every job of a workflow needs the same permissions, set exactly those scopes once at the top level (never `write-all`). The guide's `scorecard.yml` now uses top-level `contents: read` (was `read-all`).
- PULUMI-05: `cfg.GetObject` is allowed when the whole config key is optional.
- COMMIT-05: `ci`, `deps` and `release` are scopes, never types.
- K8S-02: a file may bundle the tightly coupled resources of one app and carry the app name (exception to `<kind>-<name>.yaml`).
- K8S-11: certificate through the `ListenerSet` annotation; Gatus annotation on Helm-values routes, on hand-written `HTTPRoute` manifests only when the app should be probed.
- COMMIT-02: `perf` joins the types; COMMIT-19: both release commit forms are named.
- DOC-18 (new): text meant to be copied goes in a fenced code block, not inline.
- K8S-12: only values shared by more than one manifest go into `cluster-configuration.yaml`, which the owner usually edits; a single-use value may stay a literal.
- README-03: the OpenSSF Scorecard badge comes from `api.scorecard.dev`, the other badges from shields.io.
- README-05: mise is linked once in Requirements and named without a second link in the Development opener (resolves a conflict with DOC-03).
- New Repository Checklist: the secret scan runs in CI too.
- K8S-11 and K8S-10 (ExternalSecret) no longer name a third party's annotation key or API version; Working Rules, `style-audit` and `style-update` now say to name such keys and fields only when the owner requires them and a review would miss them, and never API versions.
- Install script replaces only links into this repository; the README gained install caveats, usage, model choice, token load and how to change or extend the guide; the global instruction is a copyable block.
- Consistency fixes: sources rows for YAML, CONF and MAKE, Nix evidence wording, conform note in COMMIT-20, AI trailer wording, skills stop with a clear message when no guide root exists.
- New Repository Checklist (principles README, shown in the `repo-setup` digest): a soft list of default files, not a rule.

## 2026-11-18

- Initial rule set, reviewed by two independent audits and the owner's interview.
- All open questions answered and recorded as `stated` rules.
- GO-30 to GO-37 are now PULUMI-01 to PULUMI-08.
- K8S-17 and K8S-18 are now YAML-03 and YAML-04; K8S-19 to K8S-21 are CONF-01 to CONF-03; K8S-14 and K8S-16 are RENOV-05; the other K8S rules were renumbered K8S-01 to K8S-13 before the first publication, so older K8S numbers outside the guide do not map. Retired IDs: `common/retired.txt`.
- New families: PULUMI, YAML, CONF, MAKE.

# YAML

Deltas against `../principles/` for all YAML files: manifests, values, workflows, Home Assistant and Renovate-adjacent config. Kubernetes-specific rules are in `yaml-kubernetes.md`.

## YAML-01 · must · yaml · observed

- Rule: Start every YAML file with `---`; add a `# yaml-language-server: $schema=<url>` line next to it for Flux, Kustomize and Helm resources and chart values.
- Good: `---` then `# yaml-language-server: $schema=https://example.com/kustomization.json` then `resources:`.
- Bad: a Kustomization file that starts directly with `resources:`.
- Source: 829 of 831 files start with `---`; 475 carry a modeline.
- Check: tool:yamllint (`document-start`)

## YAML-02 · prefer · yaml · observed

- Rule: Quote strings YAML would misread (`"true"`, `"5432"`, `"01:00"`, `"${VAR}"`); leave other strings bare.
- Source: mealie `configmap-env.yaml`; quoting of plain emails and URLs is inconsistent.
- Check: judgment (yamllint `truthy` helps)

## YAML-03 · must · yaml · observed

- Rule: Use two-space indentation, sequences indented under their key, a blank line between logical blocks in values files, a final newline and no trailing spaces.
- Good: `items:` followed by `- name: a` indented two spaces under the key, one blank line between blocks.
- Bad: `items:` with `- name: a` flush left, four-space indents, trailing spaces.
- Source: two-space indentation and a leading `---` in the cluster app values and the infrastructure repos; yamllint (extends default) is configured in 4 of 5 spot-checked repos (applications, infrastructure, Home Assistant configuration, github-infrastructure).
- Check: tool:yamllint

## YAML-04 · prefer · yaml · stated

- Rule: Run `yamllint .` in every repo with `extends: default` in a file named `.yamllint.yml`, using the long rule family (`line-length` off) in new repos. Observed: set `empty-lines.max: 2` and braces and brackets `max-spaces-inside: 1`.
- Why: two families exist with different line lengths (350, 180, 225, 100, off); long is the choice for new repos.
- Source: stated 2026-11-18, yamllint file name and rule family. Observed details: the `empty-lines` and `max-spaces-inside` settings. Evidence: 11 repos with `.yamllint.yml`, 6 with `.yamllint`, 2 with `.yamllint.yaml`.
- Check: tool:yamllint

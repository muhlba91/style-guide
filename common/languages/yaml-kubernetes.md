# YAML and Kubernetes

Deltas against `../principles/`. Evidence: home-cluster applications (2102 owner commits), infrastructure, k8s-demos, HA configuration, container repos, DNS repos. The untrailered 2026-09-30 sweeps `e093196d` and `4cf96084` look tool-assisted and weigh 0.5 (cap `prefer`, never raise a rule alone); the owner wrote the subjects and README text. Do not encode pre-2026 shapes (Argo CD, Ingress, `.yml` manifests).

Rules for all YAML are in `yaml.md`. Dockerfiles, DNS zone files and Home Assistant YAML are in `config-other.md`.

## K8S-01 · prefer · kubernetes · observed

- Rule: In Flux app repos, lay out an app as `<scope>/<group>/<app>/{kustomization.yaml, namespace.yaml, app/, extensions/}`: `app/` holds `ks.yaml`, `kustomization.yaml`, `kustomizeconfig.yaml`, `values.yaml` and `templates/{release,repository}.yaml`; `extensions/` holds its Flux `ks.yaml` and all non-Helm manifests. Shared apps live in `common/<group>/<app>`, site-specific in `sites/<site>/<group>/<app>`.
- Why: repo-specific, one repo (home-cluster applications).
- Source: all 40+ app directories; consolidated `4cf96084` (2026-09-30).
- Check: judgment

## K8S-02 · must · kubernetes · stated

- Rule: Name manifest files `<kind>-<name>.yaml` in lowercase kebab-case with the `.yaml` extension. Exception: a file may bundle the tightly coupled resources of one app and carry the app name when the folder context makes the kinds clear (`external-services/app/templates/paseo.yaml`).
- Good: `external-secret-mealie-db.yaml`, `postgresql-backup.yaml`; `paseo.yaml` bundling the Service, EndpointSlice, ListenerSet, HTTPRoute and TrafficPolicy of one external service.
- Bad: `Secret_Mealie.yml`
- Source: stated 2026-11-19, bundled files for tightly coupled app resources. Evidence: `.yaml` manifests in 4 of 5 manifest repos (home-cluster applications 835 against 4 `.yml`, infrastructure 19 against 1, kubernetes-applications 78 against 1, Home Assistant configuration 60 against 1); the teaching k8s-demos are mixed. The `.yml` to `.yaml` rename `4cf96084` is untrailered (weight 0.5), the counts are the independent source. Workflow files stay `.yml` (CI-08).
- Check: judgment

## K8S-03 · prefer · kubernetes · observed

- Rule: Define each Flux `Kustomization` with `name: &application <app>`, pass `APPLICATION: *application` and the namespace through `postBuild.substitute`, and set `interval: 10m`, `retryInterval: 2m`, `prune: true`, `wait: false`; name the extension kustomization `<app>-extensions`.
- Why: repo-specific, one repo (home-cluster applications).
- Source: 112 files use `&application`.
- Check: judgment

## K8S-04 · prefer · kubernetes · observed

- Rule: Deploy Helm charts as an `OCIRepository` plus a `HelmRelease` with `chartRef` and values in a ConfigMap via `valuesFrom`; set `maxHistory: 3`, `install.strategy: RetryOnFailure`, `upgrade.remediation.retries: -1` and `rollback.recreate: true`.
- Why: repo-specific, one repo, one tool-assisted sweep.
- Source: `release.yaml` identical across about 40 apps (sweep `e093196d`, 2026-09-30, untrailered, weight 0.5).
- Check: judgment

## K8S-05 · prefer · kubernetes · observed

- Rule: Use the bjw-s `app-template` for apps without a good upstream chart and key everything by app name; write image `repository`, `pullPolicy: IfNotPresent` and `tag` as separate keys and leave a blank line between `image`, `envFrom`, `env`, `resources` and `probes`.
- Why: a uniform values shape across apps.
- Source: mealie, immich, litellm, qdrant; stable since 2024-12.
- Check: judgment

## K8S-06 · prefer · kubernetes · stated

- Rule: Set `requests.cpu`, `requests.memory` and `limits.memory` on every container, derive values from measured recommendations (KRR), and set no CPU limit unless a measured need exists.
- Why: 149 memory limits against 10 CPU limits (GPU, gateway, immich, grafana and others); operators and old apps differ.
- Good: cpu `10m`, memory `396Mi`, memory limit `512Mi`.
- Bad: round guesses and a CPU limit without a measured need.
- Source: stated 2026-11-18, resource policy. Evidence: values files; 12 "update resources" commits (2026-08), repeated OOM fixes.
- Check: judgment

## K8S-07 · lean · kubernetes · observed

- Rule: Define probes once with an anchor (`liveness: &server_probes`), reuse it for readiness, use `custom: true` with explicit `httpGet`, and disable `startup` unless needed.
- Source: mealie, immich; 2 to 3 apps checked.
- Check: judgment

## K8S-08 · must · kubernetes · stated

- Rule: Protect stateful resources of new apps from Git deletion: namespaces and databases carry `kustomize.toolkit.fluxcd.io/prune: disabled` with a one-line guardrail comment, and PVCs set `retain: true` with a reason; add it to older apps when you touch them.
- Why: introduced 2026-09-30 (`e093196d`), tool-assisted; repo-specific: one repo.
- Good: a new database namespace with `kustomize.toolkit.fluxcd.io/prune: disabled` and a one-line comment saying why.
- Bad: a new stateful app whose namespace or PVC can be pruned by Flux.
- Source: stated 2026-11-18, stateful guardrails. Evidence: 10 guardrail comments; mealie and litellm namespaces.
- Check: judgment

## K8S-09 · prefer · kubernetes · observed

- Rule: Give each app database a CloudNativePG `Cluster` named `<app>-postgresql` with explicit `resources`, `stopDelay: 300`, a backup and objectstore pair, a credentials ExternalSecret and a `# renovate:` comment above `imageName`; keep a commented-out `initdb` block beside the active `recovery` block as a deliberate switch, not dead code (PRIN-17).
- Why: one database shape for every app.
- Source: mealie, litellm, immich, HA.
- Check: judgment

## K8S-10 · prefer · kubernetes · observed

- Rule: Create one `ExternalSecret` (the cluster's current API version, store `vault-auth`) per consumer secret and spell out `conversionStrategy: Default`, `decodingStrategy: None`, `key` and `property`; use SOPS only for bootstrap (`secret-*.enc.yaml`).
- Why: repo-specific: one repo (home-cluster applications).
- Source: all `external-secret-*.yaml`. See PRIN-26.
- Check: judgment (gitleaks catches committed secrets, not this layout)

## K8S-11 · prefer · kubernetes · stated

- Rule: Expose apps through Gateway API (`ListenerSet`, `HTTPRoute`) with external-dns and cert-manager annotations fed by Flux variables; cert-manager issues the certificate through the `ListenerSet` annotation, not a separate `Certificate`. Set the Gatus enabled annotation on routes that Helm values define; on a hand-written `HTTPRoute` manifest add it only when the app should be probed.
- Source: stated 2026-11-19, Gatus annotation scope and certificate through the `ListenerSet` annotation. Evidence: migration `e25fb258` family (2026-05-04), human subjects; 2 of 12 hand-written `HTTPRoute` manifests carry the Gatus annotation, 32 files with Helm values do.
- Check: judgment

## K8S-12 · prefer · kubernetes · stated

- Rule: Define per-site values that more than one manifest uses once in `cluster-configuration.yaml` as SCREAMING_SNAKE variables grouped under lowercase comment headers; a value used by one manifest may stay a literal there (an exception to PRIN-25). The owner usually adds the entries by hand: propose a new variable instead of editing the file unprompted.
- Source: stated 2026-11-19, shared per-site values only, entries added by the owner. Evidence: `sites/*/app-of-apps/cluster-configuration.yaml`. See PRIN-25.
- Check: judgment

## K8S-13 · prefer · kubernetes · observed

- Rule: Kubernetes: write section headers in flat config maps as lowercase noun phrases; other comments follow PRIN-15.
- Why: typical why comments are a guardrail, a workaround with link or an operator quirk.
- Source: about 85 distinct comments in the manifests; all lowercase without period.
- Check: judgment

## Avoid (AI-Era Artifacts)

- AI-era artifacts: commented-out options kept as leftovers (`# ipFamilyPolicy: PreferDualStack` x5); only deliberate switches stay.
- Emoji or box-drawing in validation script output.
- Vague repeated commit subjects for tuning runs (see COMMIT-12).

## Not Covered

Helm `values.yaml` bodies beyond mealie, immich and litellm; HA `common/configuration` contents; the internals of one teaching site.

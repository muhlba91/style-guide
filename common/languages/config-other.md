# Other Config

Deltas against `../principles/` for Dockerfiles, DNS zone files and Home Assistant YAML. Thin evidence: skimmed, not read in depth.

## CONF-01 · lean · config · observed

- Rule: Pin Dockerfile base images by tag and digest, set the full `org.opencontainers.image.*` label set with one `LABEL` per line, and run hadolint with a `.hadolint.yml` whose ignores carry a reason.
- Source: pgvecto and node-red container repos.
- Check: tool:hadolint

## CONF-02 · lean · config · observed

- Rule: Keep DNS zones one file per zone in octoDNS format with a `# <Service>: <what>` comment above each service block.
- Source: muehlbachler-dns-global; one repo family.
- Check: judgment

## CONF-03 · lean · config · observed

- Rule: Split Home Assistant configuration by domain directory (`automation/<room>/<name>.yaml`, `packages/`) with `common/` and `sites/<site>/`; use `alias: "Room: Purpose"` and blueprints for repeated logic.
- Source: HA configuration tree, skimmed only.
- Check: judgment

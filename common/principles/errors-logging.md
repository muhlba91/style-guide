# Errors and Logging

## PRIN-29 · lean · common · observed

- Rule: Handle or log an error once, where it is handled; do not swallow it silently.
- Why: log-then-return and wrap-and-return both occur; see GO-12 and PULUMI-02 for the language split.
- Source: Go services and Pulumi programs, Python client (log and return `None`); some `_` discards in Pulumi helpers are counter-evidence.
- Check: tool:golangci-lint (`errcheck`, Go only)

## PRIN-30 · prefer · common · observed

- Rule: Log with the language's logger using placeholders or structured fields, never string concatenation, f-strings or `print`; prefix messages with the area when the program is flat.
- Good: `_LOGGER.error("Could not call API %s", path)`; `[google][project] error creating project`.
- Bad: `print("error " + path)`
- Source: Python `_LOGGER` with lazy `%s` placeholders in all modules of both repos (0 prints, 2021-2026; one project family); Go zerolog bracket prefixes (about 156 calls, 4 repos); shell `[module]` tags.
- Check: tool:golangci-lint (`sloglint`, Go slog only); otherwise judgment

## PRIN-31 · prefer · common · observed

- Rule: Use levels by meaning: debug for per-event detail, info for milestones and executed commands, warning for recoverable problems, error for lost operations.
- Source: onyx-homeassistant-integration and onyx-client, 2021-2026.
- Check: judgment

## PRIN-32 · must · common · stated

- Rule: Write log messages lowercase without a trailing period, in every language; free-text error messages follow the same form, while error codes, machine-readable identifiers, acronyms and code-like tokens keep their original case, also at the start.
- Why: the Home Assistant integration and Go already do; the Python library used sentence case with a period and changes when touched.
- Good: `failed to create the client: %w`; `error creating project: <name>` (failing operation, then the offending value); the code `ONYX_ACTION_ERROR` stays uppercase.
- Bad: `Error!`; `Failed to create the client.`
- Source: stated 2026-11-18, log message case. Observed details: the message names the failing operation and the offending value. Evidence: Go adguard, watermeter (`%q` values); Python library (sentence case) and integration (lowercase), each stable since 2021 or 2023.
- Check: judgment

## PRIN-33 · must · common · observed

- Rule: Remove debug prints before committing.
- Good: the commit contains only the fix; the `print(resp)` used while debugging is gone.
- Bad: `print("here", resp)` left in the client code.
- Source: onyx-client `f267b8c`, `5b14d2a` (2021, human); 0 prints in source today.
- Check: judgment

## PRIN-34 · lean · common · observed

- Rule: Never write credentials into a log line, repr or exception text.
- Source: onyx repos, Nov 2026 (`describe_exception`, token masking), AI-assisted; single topic, weight 0.5. Related to PRIN-26.
- Check: judgment

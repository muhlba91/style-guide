# Python

Deltas against `../principles/`. Evidence: onyx-client (2021-2026), onyx-homeassistant-integration (2021-2026), node-red backup_restore (deprecated). No `Co-Authored-By` trailer before 2026-10, but the large Nov 2026 rewrites read as AI-assisted. The human baseline is 2021 to 2025; 2026 text shows what the owner accepts.

## PY-01 · must · python · observed

- Rule: Lint and format with ruff only, through pre-commit (`ruff --fix`, `ruff-format`) and `ruff check .` in CI; add no black, isort, flake8 or pylint.
- Why: one tool replaced a flake8 plugin stack and black (`36bea9d`, 2023, human).
- Good: `.pre-commit-config.yaml` with the `ruff --fix` and `ruff-format` hooks and `ruff check .` in CI.
- Bad: a `black` hook next to a `flake8` hook.
- Source: 3 of 3 personal Python repos.
- Check: tool:ruff

## PY-02 · prefer · python · stated

- Rule: Use ruff defaults without a `[tool.ruff]` section; a stricter `ruff.toml` (`E W F B I UP`, 120 columns, a reason comment on each ignore) applies only to script collections.
- Why: no personal repo has a ruff config; the strict one exists only in the AI-built teaching-toolkit.
- Source: stated 2026-11-18, ruff selection. Evidence: 3 repos without config; teaching-toolkit `ruff.toml` (Tier 1.5).
- Check: tool:ruff

## PY-03 · must · python · observed

- Rule: Manage projects with poetry (`pyproject.toml`, `poetry.lock`) and pin the Python constraint to the supported minor (`>=3.14,<3.15`); follow the Home Assistant minimum Python for integrations.
- Good: `python = ">=3.14,<3.15"` in `pyproject.toml` next to a committed `poetry.lock`.
- Bad: `python = "*"` or a `requirements.txt` as the only manifest.
- Source: poetry since 2021; Python minimum moved 3.8, 3.11, 3.12, 3.13, 3.14 (2021-2026) with Home Assistant.
- Check: judgment

## PY-04 · must · python · observed

- Rule: Python: set `fail_under = 95` and `show_missing = true` for PRIN-37, and run pytest with `--strict-markers --cov=<package>`.
- Good: `fail_under = 95` and `show_missing = true` under `[tool.coverage.report]`; `addopts = "--strict-markers --cov=mypkg"`.
- Bad: `fail_under = 80` or a pytest run without `--cov`.
- Source: identical block in 3 of 3 repos since 2023, human.
- Check: tool:pytest-cov

## PY-05 · prefer · python · stated

- Rule: Use no `pragma: no mutate` blocks; remove existing ones when you touch the file. Observed: run mutmut in CI and keep log lines out of mutation with a coverage exclusion and `do_not_mutate_patterns`.
- Source: stated 2026-11-18, mutation pragmas. Observed details: mutmut in CI, the exclusion mechanism. Evidence: `63843cd` (2026-08) and `b709560` (2026-11) in both main repos, mixed human and [ai]; pragma blocks remain in `client.py`.
- Check: judgment (mutmut helps)

## PY-06 · prefer · python · observed

- Rule: Group tests in a `Test<Class>` class without a base class, name methods `test_<behavior>`, add an `__init__.py` per folder, and give no docstring to test methods; a module docstring is one line.
- Source: onyx-client about 45 files, 2021-2026; HA repo per entity module.
- Check: judgment

## PY-07 · lean · python · observed

- Rule: In constructor tests assert every attribute, test defaults in a separate test, and test `__str__` with the full expected string.
- Source: `tests/device/test_shutter.py`, 2023-2024, human.
- Check: judgment

## PY-08 · prefer · python · observed

- Rule: Test async code with pytest-asyncio and `aioresponses`; use the Home Assistant pytest plugin for integrations; keep fakes in `tests/helpers.py` and fixtures in `conftest.py`.
- Source: onyx-client `5a0f32e` (2024), HA repo.
- Check: judgment

## PY-09 · lean · python · observed

- Rule: Prove with a dedicated test that secrets never reach logs, repr or exceptions, using a recognizable fake token and `caplog`.
- Source: `tests/test_client_logging.py`, `test_log_safety.py` (2026-11, [ai?]); single feature.
- Check: judgment

## PY-10 · prefer · python · observed

- Rule: One class per module, named in snake_case after the concept; group modules in packages by kind (`data/`, `device/`, `enum/`, `exception/`, `utils/`); every folder has an `__init__.py` with a one-line docstring.
- Why: a predictable place for every class.
- Source: both repos, all years; one project family. Supporting, AI-generated: recording-transcriber uses the same package layout.
- Check: judgment

## PY-11 · prefer · python · observed

- Rule: Order imports standard library, third party, local; use relative imports inside the package and `collections.abc` for ABCs.
- Good: `from ..const import DOMAIN`
- Bad: `from onyx_client.const import DOMAIN` inside `onyx_client/`
- Source: `5be6160` (2023-12, human), `dfd8c9c` (2026). Tests import absolutely. ruff `I` is not enabled, so no tool checks this. One project family. Supporting, AI-generated: recording-transcriber uses relative imports.
- Check: judgment

## PY-12 · prefer · python · stated

- Rule: Run pyright in CI of new Python projects. Observed: annotate public signatures with modern syntax (`X | None`, `list[str]`), never `Optional` or `typing.List`.
- Why: no checker runs in the existing repos; new projects add one.
- Source: stated 2026-11-18, type checker (pyright). Observed details: standard mode, modern syntax. Evidence: 2021 code used `Optional`; `dfd8c9c` (2026-08) converted.
- Check: judgment

## PY-13 · must · python · stated

- Rule: Give every module, class and public function a docstring: a one-line summary with a period, then one `name: description` line per parameter, even an obvious one, without `Args:` and without types; this API documentation overrides PRIN-05 and PRIN-14.
- Why: callers must know from the rendered docs what each argument does. Types live in the signature.
- Good: `identifier: the device identifier to cancel the command for`
- Bad: an `Args:` block with types.
- Source: stated 2026-11-18, parameter lines. Evidence: 70+ modules since 2021, parameter block from 2023; AI-era files keep the format.
- Check: judgment

## PY-14 · prefer · python · stated

- Rule: Close a multi-line docstring on the last text line, in all Python code.
- Why: the library has done so since 2021; the 2026 integration docstrings that close on their own line are AI-era.
- Source: stated 2026-11-18, docstring quotes. Evidence: library `Parameters` blocks versus HA 2026 docstrings.
- Check: judgment

## PY-15 · prefer · python · observed

- Rule: Refer to methods in docstrings as `::name` and state behavioral contracts (raised errors, state kept on failure) in the docstring, not in comments.
- Source: onyx-client `client.py` since 2021.
- Check: judgment

## PY-16 · prefer · python · stated

- Rule: End exception names in `Exception`, not `Error`. Observed: use snake_case modules and functions, PascalCase classes, UPPER_SNAKE constants in `const.py`, and a leading underscore to mark internals (`_helper`, `self._client`); dunder methods (`__str__`) and `_LOGGER = logging.getLogger(__name__)` are fine.
- Why: the `Exception` suffix is consistent since 2021 and kept on purpose, against PEP 8 and ruff `N818`.
- Source: stated 2026-11-18, exception suffix. Observed details: the other naming conventions. Evidence: all modules, 2021-2026; one project family. Supporting, AI-generated: recording-transcriber uses `_LOGGER`.
- Check: judgment

## PY-18 · must · python · stated

- Rule: Python: write log messages lowercase without a period in new or substantially rewritten code and fix existing ones when you touch them (PRIN-32).
- Good: `"adding %s hella_onyx light entities"`
- Source: stated 2026-11-18, log message case. Evidence: HA `__init__.py`, `cover.py`; library `client.py` still uses sentence case.
- Check: judgment

## PY-19 · lean · python · observed

- Rule: Example only, not a rule: onyx-client returns `None` or `False` and logs on an unusable API response, and raises only for rejected credentials or invalid configuration.
- Source: `client.py` since 2021; API design of one library.
- Check: judgment

## PY-20 · prefer · python · observed

- Rule: Catch specific exception types, chain with `raise ... from ex`, and use broad `except Exception` only at a task boundary with a logged reason.
- Source: `client.py`, HA `api_connector.py`; mostly AI-era, weight 0.75.
- Check: judgment (ruff `BLE001` helps if selected; nothing is selected)

## PY-21 · prefer · python · observed

- Rule: Prefer plain literals and `.get("key")`: `[]` not `list()`, no redundant `None` default, `is None` checks.
- Source: `63843cd`, `dfd8c9c` (2026), committed by the owner; 2021-2024 code used the long forms.
- Check: judgment (ruff `C408` helps if selected; nothing is selected)

## PY-22 · lean · python · observed

- Rule: Example only, not a rule: onyx-client v12 uses `asyncio.timeout` and async iteration and leaves the session and loop to the caller.
- Source: onyx-client v12 migration list; API design of one library.
- Check: judgment

## PY-23 · prefer · python · observed

- Rule: In integrations follow the upstream Home Assistant developer documentation.
- Why: the integration restates upstream requirements; the docs are the source, not this guide.
- Source: both integration snapshots (2024, 2026) follow them.
- Check: judgment

## PY-24 · prefer · python · observed

- Rule: Publish libraries with `poetry-core`, trusted publishing and release-please; an integration uses `package-mode = false` and pins the library version in `manifest.json`.
- Source: `b747f7c`, `0439942` (2023), 3 of 3 repos; one project family.
- Check: judgment

## PY-25 · lean · python · observed

- Rule: Example only, not a rule: the deprecated node-red backup_restore CLI uses `click` with one function per command.
- Source: one deprecated repo.
- Check: judgment

## PY-26 · prefer · python · stated

- Rule: Use `@dataclass` for new value objects that compare all fields; keep plain classes for entities that compare by identifier or run logic in `__init__`; leave existing classes unchanged.
- Why: a dataclass generates `__init__`, `__repr__` and field-wise `__eq__`, which matches the value objects in `data/`; Group and Device compare by `identifier` alone, which a default dataclass would change.
- Source: stated 2026-11-18, dataclasses. Observed details: `slots=True` and field docs as `name: description` lines in the class docstring. Evidence: library classes with hand-written `__eq__` (9 value objects compare all fields, 2 entities compare the identifier); the integration uses one `@dataclass`.
- Check: judgment

## Avoid (AI-Era Artifacts)

- `Args:` and `Returns:` docstrings, and long explanatory docstrings, beyond summary plus parameters.
- `pragma: no mutate` blocks around log calls.
- Comments above every constant in new code beyond reason or unit.

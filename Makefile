# Quality gate of the style guide. Run `make check` when a change is finished.

PYTHON       ?= python3
SHELLCHECK   ?= shellcheck
MARKDOWNLINT ?= markdownlint-cli2
YAMLLINT     ?= yamllint

SHELL_SCRIPTS := $(wildcard scripts/*.sh)

.DEFAULT_GOAL := help
.PHONY: help check lint lint-shell lint-markdown lint-yaml rules digest digest-check test skills install

help:  ## list the targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-16s %s\n", $$1, $$2}'

check: lint rules digest-check test  ## everything a finished change must pass
	@echo "ALL CHECKS PASSED"

lint: lint-shell lint-markdown lint-yaml  ## all linters, read-only

lint-shell:  ## shellcheck on the scripts
	$(SHELLCHECK) -x $(SHELL_SCRIPTS)

lint-markdown:  ## markdownlint (.markdownlint.yaml)
	$(MARKDOWNLINT) "**/*.md" "#LICENSE.md" "#work" "#.mise" "#node_modules" "#common/digest"

lint-yaml:  ## yamllint (.yamllint.yml)
	$(YAMLLINT) --strict .

rules:  ## structure and content checks of the rule files (scripts/check_rules.py)
	$(PYTHON) scripts/check_rules.py

digest:  ## generate the lean digests in common/digest/ from the rule files
	$(PYTHON) scripts/build_digest.py

digest-check:  ## digests are current and within the token budgets
	$(PYTHON) scripts/build_digest.py --check

test:  ## tests of the rule checker
	$(PYTHON) -m unittest discover -s tests -v

skills:  ## recreate the relative skill links in .agents/skills and .claude/skills
	scripts/link-skills.sh

install:  ## link the skills into the agent skill folders of this machine (see scripts/install.sh)
	scripts/install.sh

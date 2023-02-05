ifeq ($(UNAME),Darwin)
	SHELL := /opt/local/bin/bash
	OS_X  := true
else ifneq (,$(wildcard /etc/redhat-release))
	OS_RHEL := true
else
	OS_DEB  := true
	SHELL := /bin/bash
endif

.PHONY: help
all: help

init_translations: ## Init translations
	pybabel extract -F babel.cfg -o translations/messages.pot .
	pybabel init -i translations/messages.pot -d translations -l de -l nl -l fr

update_translations: ## Update translations
	pybabel update -i translations/messages.pot -d translations

compile_translations: ## Compile translations
	pybabel compile -d translations

build_docker: ## Build docker
	docker build -t boxespy-flask .

run_docker: ## Run in docker
	docker run -ti -p 8001:8001 boxespy-flask:latest

help:
	@## http://www.network-science.de/ascii/ ; Font: smslant; Adjustment: left; Stretch: yes; Width: 120;
	@echo '______                                             '
	@echo '___  /___________  ______________ _____________  __'
	@echo '__  __ \  __ \_  |/_/  _ \_  ___/ ___  __ \_  / / /'
	@echo '_  /_/ / /_/ /_>  < /  __/(__  )____  /_/ /  /_/ / '
	@echo '/_.___/\____//_/|_| \___//____/_(_)  .___/_\__, /  '
	@echo '                                  /_/     /____/   '
	@echo ''
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo ''

# Makefile для проекта поиска дубликатов телефонов
# Использование: make <target>, список целей — make help

.PHONY: help install run lint format format-check typecheck fullcheck test fulltest precommit precommit-run clean

# Переопределяемые переменные
PYTHON   ?= python
RUFF     ?= ruff
PYRIGHT  ?= pyright
DATA     ?= data.txt

## Показать список доступных команд
help:
	@echo "Доступные команды:"
	@echo "  make install       - установить инструменты разработки"
	@echo "  make run           - запустить скрипт на data.txt"
	@echo "  make lint          - проверить код линтером Ruff"
	@echo "  make format        - отформатировать код и применить автофиксы"
	@echo "  make format-check  - проверить форматирование без изменений"
	@echo "  make typecheck     - проверить типы через Pyright"
	@echo "  make fullcheck     - все статические проверки"
	@echo "  make test          - запустить тесты"
	@echo "  make fulltest      - статические проверки + тесты"
	@echo "  make precommit     - установить git hooks"
	@echo "  make precommit-run - прогнать все хуки вручную"
	@echo "  make clean         - удалить кеши"

## Установить инструменты разработки
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install ruff pyright pytest pre-commit

## Запустить скрипт
run:
	$(PYTHON) script.py $(DATA)

## Линтер
lint:
	$(RUFF) check .

## Форматирование и автофиксы
format:
	$(RUFF) format .
	$(RUFF) check --fix .

## Проверка формата (без изменений на диске)
format-check:
	$(RUFF) format --check .

## Проверка типов
typecheck:
	$(PYRIGHT)

## Все статические проверки
fullcheck: lint format-check typecheck
	@echo === Все статические проверки пройдены ===

## Тесты
test:
	$(PYTHON) -m pytest -v

## Полная проверка: статика + тесты
fulltest: fullcheck test
	@echo === Полная проверка пройдена ===

## Установить git hooks (pre-commit и pre-push)
precommit:
	$(PYTHON) -m pre_commit install --hook-type pre-commit --hook-type pre-push

## Прогнать все pre-commit хуки вручную (для всех файлов)
precommit-run:
	$(PYTHON) -m pre_commit run --all-files

## Очистка кешей (кросс-платформенно, через Python)
clean:
	$(PYTHON) -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]"
	$(PYTHON) -c "import shutil, pathlib; [shutil.rmtree(p) for p in [pathlib.Path('.ruff_cache'), pathlib.Path('.pytest_cache')] if p.exists()]"
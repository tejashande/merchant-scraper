.PHONY: install test test-cov lint format type-check clean run

# Development
install:
	pip install -r requirements/dev.txt

test:
	pytest tests/

test-cov:
	pytest tests/ --cov=src --cov-report=term-missing

lint:
	autoflake --in-place --remove-all-unused-imports -r src tests
	isort src/ tests/
	black src/ tests/
	flake8 src tests

format:
	black src tests
	isort src tests

type-check:
	mypy src tests

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +

# Running
run:
	python scripts/run_scraper.py "Haarlem, Netherlands" --radius 5000

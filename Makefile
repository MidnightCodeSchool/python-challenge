# Test all challenges
test-all:
	pytest -v

# Test one challenge
# Usage: make test C=000
test:
	@if [ -z "$(C)" ]; then echo "C is not set"; exit 1; fi
	pytest -v tests/test_p$(C).py

install:
	-pipx install poetry
	poetry install --with=dev
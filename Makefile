C ?=000

test%:
	echo $*
	pytest -v tests/test_p$(*).py

# Test all challenges
test-all:
	pytest -v

# Test one challenge
# Usage: make test C=000
test: test"$(C)"

install:
	-pipx install poetry
	poetry install --with=dev
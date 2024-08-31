test:
	pytest -v

install:
	-pipx install poetry
	poetry install --with=dev
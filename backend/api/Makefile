install:
	pip install -r requirements.txt

style:
	python -m black --line-length 79 .

lint:
	python -m flake8

test:
	python -m unittest

start:
	sam local start-api --port 2999

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

migrate:
	sam local invoke --no-event --docker-network sam_local MigrationTool 

create-migration:
	# eg. make create-migration name=create_table
	python -m src.scripts.create_migration --name $(name)

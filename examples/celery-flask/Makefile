clean-python:
	find . -name __pycache__ | xargs rm -rf

clean-docker:
	docker-compose kill
	docker-compose rm -fv --all

clean: clean-docker clean-python

build:
	docker-compose build --no-cache

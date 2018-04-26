install:
	pip install -r requirements.txt
	pip install src/TaskRunner/
	pip install src/FetchService

lint:
	pylint src

test:
	python -m pytest src

check: install lint test

clean:
	pip uninstall -r requirements.txt -y
	pip uninstall FetchService -y
	pip uninstall TaskRunner -y


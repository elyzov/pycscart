build: clean check
		pip install wheel
		python setup.py sdist bdist_wheel

check:
		tox -e pep8
		tox -e test-py26
		tox -e test-py27
		tox -e test-py33

publish: build
		pip install twine
		twine upload dist/*

clean:
		rm -rf dist/ build/

.PHONY: itests test clean package publish

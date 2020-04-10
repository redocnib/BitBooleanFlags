clean:
	rm -f *.pyc *.class
	rm -rf __pycache__
	rm -rf dist build bit_boolean_flags.egg-info

build:
	python setup.py sdist bdist_wheel
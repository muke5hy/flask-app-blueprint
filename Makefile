.PHONY: tests

all: venv install

bootstrap: 
	echo "Installing Pip"
	sudo apt-get install python-pip
	echo "Installing virtualenv"
	sudo pip install virtualenv
	sudo pip install nose

venv:
	virtualenv .venv -p python3

tests:
	nosetests -v tests

install:
	echo "Installing packages from requirements.txt"
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python run.py

clean:
	rm *.pyc

requirements:
	echo "Updating requirements.txt"
	pip freeze > requirements.txt
# Project Title

This is a simple Flask application for storing and getting ToDo tasks.
It uses Flask and SQLite.  
We're going to write some tests for it.

## Getting Started

* Clone this repo

### Prerequisites

You will need Python(I have 3.7 on my machine, but 3.5+ will work), also pip for installation packages.

### Installing
* If you don't have virtualenv, you should install it.
```
pip install virtualenv
```
* Create a virtual environment
```
python -m venv name_of_your_virtual_env
```
* Activate it
```
source name_of_your_virtual_env/bin/activate
```
* Add to the environment variable PYTHONPATH to direcrory with cloned repo:
```
export PYTHONPATH="${PYTHONPATH:+/Path/to/this/repo/pytest-aug2019}"
```
* Install required libs in your virtual environment:
```
pip install -r requirements.txt
```

## Running the tests

* Go to application folder:
```
cd application

```
* Run tests all the tests:
```
pytest

```


### Break down into end to end tests

* e2e tests should be placed in `application/tests/tests_e2e.py`
* Tests with mocked database should be placed in `application/tests/tests_db_mocked.py`


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

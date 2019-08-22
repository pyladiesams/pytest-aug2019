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
* Set the config environment variable:

```
export APP_SETTINGS=config.py
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

## Plan for a workshop

* Create a test folder and a file contftest.py. We will need to put some fixtures there.
* Create a fixture for a test client.  On a set up it should create a db and start client application, on a teardown it should drop the database.
* We can set scope this feature to a module.
* Now create a test file and a test case for a creation a task with a particular text and date. Parametrise it.
* Create a test case for getting task by id (positive and negative). Try to make it one test case using parametrisation. (Hint) We also can use pytest.raise in parameters.
* Create a test case that we’ll now will fail and mark it as an xfail
* (We can create more of them just to get a grip)
* We kinda finished with e2e test, now we can start with mock part. Create a  folder with tests with mocks. It will need a separate conftest.py
* Create a test client with mocked db part.
* Create  a test case for inserting task using this client
* Create a test case for getting list of tasks using this client
* Let’s mark e2e test cases as e2e and run them separately
* In main conftest.py create a flag for e2e tests.
* Mark e2e tests with decorator for this flag.


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

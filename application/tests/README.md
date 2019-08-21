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

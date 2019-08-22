import os
import tempfile
import pytest

from application.app import db, app

@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/"

@pytest.fixture
def client():
    test_db, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.init_app(app)
        db.create_all()

    yield client
    with app.app_context():
        db.drop_all()

    os.close(test_db)
    os.unlink(app.config['DATABASE'])


def pytest_addoption(parser):
    parser.addoption(
        "--run-e2e", action="store_true", default=False, help="run e2e tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark test as e2e")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-e2e"):
        return
    skip_slow = pytest.mark.skip(reason="Run with --run-e2e flag")
    for item in items:
        if "e2e" in item.keywords:
            item.add_marker(skip_slow)

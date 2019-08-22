from datetime import datetime
import pytest
from flask import jsonify

from application.app import db, app

class MockedTask():
    def __init__(self, task_id, text, date):
        self.id = task_id
        self.text = text
        self.date = date
        __call__ = lambda x:x

    @property
    def serialize(self):
        return {
        'id': self.id,
        'text': self.text,
        'date'  : self.date.strftime("%Y-%m-%d %H:%M")}

@pytest.fixture
def client_mocked(mocker):
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch(
    "application.app.get_task",
    return_value=MockedTask(1, "mock", datetime.now()))
    client = app.test_client()
    return client

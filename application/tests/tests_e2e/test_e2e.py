import requests
import pytest

from datetime import datetime

def post_task(base_url, client, text, date):
    url = base_url + "tasks/post"
    res = client.post(
    url, data=
    {'text':text,
    'date':date.strftime("%Y-%m-%d %H:%M")})
    return res

@pytest.mark.slow
@pytest.mark.parametrize(
    "text", ["test_text", "%$#$%^&*()"])
def test_create_task(base_url, client, text):
    res = post_task(base_url,
    client, text, datetime.now())
    assert res.status_code == 200

@pytest.mark.parametrize(
    "task_id, status_code", [("a", 404), (1, 200)])
def test_get_task_by_id(base_url, client, task_id, status_code):
    post_task(base_url, client, "text", datetime.now())
    url = base_url + "tasks/" + str(task_id)
    res = client.get(url)
    assert res.status_code == status_code

@pytest.mark.xfail
def test_get_task_empty_list(base_url, client):
    url = base_url + "tasks/1"
    res = client.get(url)
    assert res.status_code == 200


def test_get_tasks_list_empty(base_url, client):
    url = base_url + "tasks"
    res = client.get(url)
    assert res.status_code == 200
    assert len(res.json["tasks"]) == 0

def test_get_tasks_list_not_empty(base_url, client):
    post_task(base_url, client, "text", datetime.now().replace(tzinfo=None))
    url = base_url + "tasks"
    res = client.get(url)
    todo = {
         'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
         'id': 1,
         'text': 'text'}
    assert res.status_code == 200
    assert len(res.json["tasks"]) == 1
    assert todo in res.json["tasks"]

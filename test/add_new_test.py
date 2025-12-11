import requests


def test1_add():
    new_task = {"title": "Task", "completed": False}
    response = requests.post(
        "https://todo-app-sky.herokuapp.com/", json=new_task)

    assert response.status_code == 202

    task = response.json()
    assert task['title'] == "Task"
    assert task['completed'] is False

    new_task = {"completed": True}
    requests.patch("https://todo-app-sky.herokuapp.com/", json=new_task)

    assert task['completed'] is True

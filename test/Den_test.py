import pytest
import requests

def add_test():
    """
    Создаем тест
    """
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)    
    response_body = response.json()

    assert response.status_code == 201
    assert response_body['completed'] == False

    id = response.json()["id"]
    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
       
    assert response.status_code == 201

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 404
    

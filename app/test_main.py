import sys
import os

# Добавляем папку app в путь импорта
sys.path.insert(0, os.path.dirname(__file__))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "ORM работает"


def test_users_empty():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
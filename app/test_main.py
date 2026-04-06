import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# Временно заменяем относительные импорты на абсолютные
import importlib.util
import inspect

# Загружаем database вручную
spec = importlib.util.spec_from_file_location("database", os.path.join(os.path.dirname(__file__), "database.py"))
database = importlib.util.module_from_spec(spec)
spec.loader.exec_module(database)

# Загружаем models
spec = importlib.util.spec_from_file_location("models", os.path.join(os.path.dirname(__file__), "models.py"))
models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(models)

# Загружаем health
spec = importlib.util.spec_from_file_location("health", os.path.join(os.path.dirname(__file__), "health.py"))
health = importlib.util.module_from_spec(spec)
spec.loader.exec_module(health)

# Загружаем main
spec = importlib.util.spec_from_file_location("main", os.path.join(os.path.dirname(__file__), "main.py"))
main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main)

from fastapi.testclient import TestClient

client = TestClient(main.app)

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
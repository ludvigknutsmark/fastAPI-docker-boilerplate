import pytest
import json

from fastapi.testclient import TestClient
from app.main import app
from app.models import User

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI boilerplate"}

def test_create_user():
    response = client.post("/users/", headers={"accept": "application/json"}, json={"username": "testuser", "password": "testpw"})
    assert response.status_code == 200
    assert response.json() == {
        "id":1, 
        "username": "testuser"
    }

    assert "password" not in response.json()
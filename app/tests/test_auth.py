import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.skip(reason="ajustar para usar Firebase de teste ou mock")
def test_register_and_login():
    email = "teste@example.com"
    password = "senhaSecreta123"

    r = client.post("/auth/register", json={"email": email, "password": password})
    assert r.status_code == 201

    r = client.post(
        "/auth/login",
        data={"username": email, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert r.status_code == 200
    data = r.json()
    assert "access_token" in data


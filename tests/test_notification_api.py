import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_notification(client):
    response = client.post('/notify/email', json={
        "to": "test@example.com",
        "message": "Your booking is confirmed!"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["to"] == "test@example.com"
    assert data["message"] == "Your booking is confirmed!"

def test_missing_fields(client):
    response = client.post('/notify/email', json={
        "to": "test@example.com"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

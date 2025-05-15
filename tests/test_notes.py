from fastapi.testclient import TestClient
from src.notes_app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert "ok" in response.json()["status"]

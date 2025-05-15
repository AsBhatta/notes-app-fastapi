from fastapi.testclient import TestClient
from notes_app.main import app

client = TestClient(app)

def test_create_note():
    payload = {
        "title": "Test Note",
        "content": "This is a test note."
    }
    response = client.post("/api/v1/notes", json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note."

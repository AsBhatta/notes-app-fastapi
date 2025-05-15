from fastapi.testclient import TestClient
from src.notes_app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code in (200, 201)
    assert "ok" in response.json()["status"]


def test_create_note():
    note_data = {
        "title": "Test Note",
        "content": "This is a test note."
    }
    response = client.post("/api/v1/notes", json=note_data)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == note_data["title"]
    assert data["content"] == note_data["content"]


def test_get_notes():
    # Create a note to ensure there is at least one
    note_data = {
        "title": "Another Note",
        "content": "Some more content."
    }
    client.post("/api/v1/notes", json=note_data)

    response = client.get("/api/v1/notes")
    assert response.status_code in (200, 201)
    notes = response.json()
    assert isinstance(notes, list)
    assert any(note["title"] == "Another Note" for note in notes)

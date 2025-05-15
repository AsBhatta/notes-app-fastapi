#  Notes App API (FastAPI)

A simple, modern RESTful API for managing notes, built with **FastAPI**.  
Ideal for learning or bootstrapping small services, this project supports:

-  Creating and retrieving notes
-  Health check endpoint
-  In-memory storage (SQLite or dummy DB)
-  Dockerized deployment
-  Pre-commit hooks for clean code
-  Test cases with Pytest
-  PostgreSQL-ready architecture

---

##  Project Structure

├── src/
│ └── notes_app/
│ ├── init.py
│ ├── config.py
│ ├── main.py
│ ├── models.py
│ └── routes.py
├── tests/
│ ├── init.py
│ ├── test_create_notes.py
| └── test_notes.py
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
├── requirements_dev.txt
├── requirements.txt
└── README.md


---

## Features

- **CRUD APIs** for managing notes
- **Health check** endpoint for status monitoring
- **Environment config** using `.env`
- **Code formatting** with Black, Flake8, isort (via Pre-commit)
- **Testing** with Pytest and FastAPI’s TestClient

---

## Environment Setup
1. Create a virtual environment:
python -m venv env
env\Scripts\activate

2. Install dependencies:
pip install -r requirements.txt

3. Run the app
uvicorn src.notes_app.main:app --reload

4. Access API docs:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

5. Run all tests using:
pytest
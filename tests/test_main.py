# import pytest

# from note_api.example import hello

# @pytest.mark.parametrize(
#     ("name", "expected"),
#     [
#         ("A. Musing", "Hello A. Musing!"),
#         ("traveler", "Hello traveler!"),
#         ("projen developer", "Hello projen developer!"),
#     ],
# )
# def test_hello(name, expected):
#     """Example test with parametrization."""
#     assert hello(name) == expected

import pytest
from fastapi.testclient import TestClient
from note_api.main import app

client = TestClient(app)

def test_get_notes():
    """Test the GET /notes endpoint."""
    response = client.get("/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_note():
    """Test the POST /notes endpoint."""
    note_data = {
        "title": "Test Note Title",        # Include title
        "description": "This is a test note.",  # Include description
        "content": "Test note"              # Include content
    }
    response = client.post("/notes", json=note_data)
    print(response.json())  # Print the response body for debugging
    assert response.status_code == 200  # Check for a successful response


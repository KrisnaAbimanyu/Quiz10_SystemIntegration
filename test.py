# test.py
import pytest
from main import app, login, subtract


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------------------------
#   API endpoint tests
# ---------------------------

def test_read_main(client):
    """
    Test the root endpoint returns 200 and correct structure.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0.0"}


def test_addition_logic(client):
    """
    Test the math endpoint to ensure logic holds.
    """
    response = client.get("/add/5/10")
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}


def test_invalid_input(client):
    """
    Test that sending text instead of integers results in 404 (Flask behavior).
    """
    response = client.get("/add/five/ten")
    assert response.status_code == 404


# ---------------------------
#   Logic function tests
# ---------------------------

def test_login_valid():
    """
    Login function works correctly with a valid account.
    """
    assert login("admin", "admin123") is True


def test_login_invalid():
    """
    Login function works correctly with invalid accounts.
    """
    # Wrong password
    assert login("admin", "wrong") is False
    # Non-existent user
    assert login("ghost", "abc") is False


def test_subtract_with_login():
    """
    Subtract function works correctly when user is logged in.
    """
    result = subtract(10, 3, True)
    assert result == 7


def test_subtract_without_login():
    """
    Subtract function should not work without login.
    """
    result = subtract(10, 3, False)
    assert result is None

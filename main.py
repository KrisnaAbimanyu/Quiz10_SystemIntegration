# main.py
from flask import Flask, jsonify

app = Flask(__name__)

# 🔹 Temporary database for login
USER_DB = {
    "admin": "admin123",
    "user": "password"
}

def login(username, password):
    """
    Login function using a temporary database.
    Returns True if the username/password is valid, otherwise False.
    """
    return USER_DB.get(username) == password


def subtract(a, b, is_logged_in):
    """
    Subtract function that can only be accessed after login.

    If is_logged_in is False, return None (or you could raise an error).
    If True, return a - b.
    """
    if not is_logged_in:
        return None
    return a - b


@app.route("/")
def root():
    """
    Root endpoint to check API health.
    """
    return jsonify({"status": "ok", "version": "1.0.0"})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """
    Simple logic function to test mathematics.
    """
    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

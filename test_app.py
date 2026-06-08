# Import the Flask app from app.py
from app import app


# This is a test function (pytest will automatically detect it)
def test_home():
    # Create a test client to simulate HTTP requests
    client = app.test_client()

    # Make a GET request to "/"
    response = client.get("/")

    # Check that the response status is 200 (OK)
    assert response.status_code == 200  # nosec B101

# Import Flask framework
# Flask is used to create a simple web server / API
from flask import Flask

# Create the Flask application instance
# __name__ tells Flask where the app is located
app = Flask(__name__)


# Define a route (URL endpoint)
# When someone visits "/", this function will run
@app.route("/")
def home():
    # Return a JSON response
    # This is what the browser/API client will see
    return {"message": "Hello DevSecOps"}


# This ensures the app runs only when executed directly
# (not when imported into another file like tests)
if __name__ == "__main__":
    # Start the web server
    # host="0.0.0.0" allows access from outside (important for Docker later)
    # port=8080 is the port where the app runs
    app.run(host="0.0.0.0", port=8080)

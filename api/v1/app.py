#!/usr/bin/env python3

from flask import Flask, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

# Flag to check if setup has been run
setup_done = False

@app.before_request
def setup():
    """Initialize storage only once before the first request"""
    global setup_done
    if not setup_done:
        storage.reload()
        setup_done = True

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the database session after each request."""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    response = {
        "error": "Not found",
        # "message": str(error)  # this is optional brother,
                                 # include the actual error message
    }
    return jsonify(response), 404

if __name__ == '__main__':
    HOST = getenv('SOS_API_HOST', '0.0.0.0')
    PORT = int(getenv('SOS_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
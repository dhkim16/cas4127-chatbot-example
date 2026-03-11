from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

# The default OLLAMA URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# CORS handling helper function
def cors_response(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

# Where the generation requests are handled
@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():

    # Handle preflight
    if request.method == "OPTIONS":
        resp = make_response("", 204)
        return cors_response(resp)

    # Get the JSON data from the request
    data = request.json or {}

    # Prepare the payload for the OLLAMA API request

    # Obtain the response from OLLAMA

    # Return the response from OLLAMA as JSON
    resp = 0 # TODO
    return cors_response(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
import os
import google.generativeai as genai
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Set the Google API key for Gemini
# Typically, you would want to set this in your environment variables rather than hardcoding it in your code for security reasons.
os.environ["GOOGLE_API_KEY"] = "YOUR API KEY HERE!"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# The Gemini model used
MODEL = "gemini-2.5-flash-lite"

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

    # Obtain the response from Gemini

    # Return the response from Gemini as JSON
    resp = 0 # TODO
    return cors_response(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)

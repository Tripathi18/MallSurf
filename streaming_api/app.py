from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
buffer = []

@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.json
    buffer.append(data)
    return jsonify({"status": "received"})

@app.route("/latest")
def latest():
    return jsonify(buffer[-50:])

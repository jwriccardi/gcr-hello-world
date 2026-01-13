import os
import json
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load quotes
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/quotes")
def get_quotes():
    return jsonify(quotes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

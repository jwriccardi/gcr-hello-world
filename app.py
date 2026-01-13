import os
import json
import random
from flask import Flask, render_template

app = Flask(__name__)

# Load quotes
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.route("/")
def hello_world():
    quote_data = random.choice(quotes)
    return render_template('index.html', quote=quote_data['text'], author=quote_data['author'])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

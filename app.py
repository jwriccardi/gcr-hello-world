import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walt Whitman</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Funnel+Display:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700&family=Quantico:wght@400;700&family=Rationale&family=Passero+One&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1a0a2e 0%, #4a1a6b 25%, #6b2d7b 50%, #4a1a6b 75%, #1a0a2e 100%);
            font-family: 'Funnel Display', sans-serif;
            padding: 2rem;
        }
        .quote-container {
            max-width: 800px;
            text-align: center;
        }
        .quote {
            font-size: clamp(1.5rem, 4vw, 2.5rem);
            font-weight: 300;
            color: #f0e6ff;
            line-height: 1.6;
            letter-spacing: 0.02em;
            text-shadow: 0 2px 20px rgba(150, 100, 200, 0.3);
        }
        .author {
            margin-top: 2rem;
            font-size: clamp(1rem, 2vw, 1.3rem);
            font-weight: 500;
            color: #c9a6ff;
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }
        .font-selector {
            position: fixed;
            bottom: 1.5rem;
            right: 1.5rem;
        }
        .font-selector select {
            background: rgba(26, 10, 46, 0.8);
            color: #c9a6ff;
            border: 1px solid #6b2d7b;
            border-radius: 6px;
            padding: 0.5rem 1rem;
            font-family: 'Funnel Display', sans-serif;
            font-size: 0.9rem;
            cursor: pointer;
            outline: none;
        }
        .font-selector select:hover {
            border-color: #c9a6ff;
        }
    </style>
</head>
<body>
    <div class="quote-container">
        <p class="quote">&ldquo;Do I contradict myself? Very well then I contradict myself, (I am large, I contain multitudes.)&rdquo;</p>
        <p class="author">— Walt Whitman</p>
    </div>
    <div class="font-selector">
        <select id="fontSelect" onchange="changeFont(this.value)">
            <option value="'Funnel Display', sans-serif">Funnel Display</option>
            <option value="'Orbitron', sans-serif">Orbitron</option>
            <option value="'Quantico', sans-serif">Quantico</option>
            <option value="'Rationale', sans-serif">Rationale</option>
            <option value="'Passero One', cursive">Passero One</option>
        </select>
    </div>
    <script>
        function changeFont(font) {
            document.querySelector('.quote-container').style.fontFamily = font;
        }
    </script>
</body>
</html>"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

import os

try:
    from flask import Flask, render_template
except ImportError as exc:
    raise ImportError(
        "Flask is not installed. Install it with `pip install flask` "
        "or activate the appropriate virtual environment."
    ) from exc

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    
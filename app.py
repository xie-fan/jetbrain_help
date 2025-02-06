from flask import Flask, send_file
from main import refresh

app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_file("index.html")

@app.route("/refresh")
def serve_refresh():
    refresh()
    return "refresh success"

if __name__ == "__main__":
    refresh()
    app.run(host='0.0.0.0', port=8000)
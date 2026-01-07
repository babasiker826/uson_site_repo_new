from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ana sayfa
@app.route("/", methods=["GET", "POST"])
def index():
    return send_from_directory(BASE_DIR, "uson.html")

# Favicon
@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return send_from_directory(BASE_DIR, "favicon.ico")

# Cloudflare RUM (sessiz geç)
@app.route("/cdn-cgi/rum", methods=["GET", "POST"])
def cf_rum():
    return "", 204

# Diğer her şey
@app.route("/<path:filename>", methods=["GET", "POST"])
def all_routes(filename):
    file_path = os.path.join(BASE_DIR, filename)

    if os.path.isfile(file_path):
        return send_from_directory(BASE_DIR, filename)

    return send_from_directory(BASE_DIR, "uson.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=False
    )

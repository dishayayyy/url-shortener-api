from flask import Flask, request, jsonify, redirect
import sqlite3
import string
import random
from urllib.parse import urlparse

app = Flask(__name__)
DB_NAME = "database.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL
            )
        """)


init_db()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc


@app.route("/")
def home():
    return "URL Shortener API with Database is running"


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data["url"]

    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()

    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
                (original_url, short_code)
            )
    except sqlite3.IntegrityError:
        return jsonify({"error": "Short code collision"}), 500

    short_url = request.host_url + short_code
    return jsonify({"short_url": short_url}), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_to_original(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "SELECT original_url FROM urls WHERE short_code = ?",
            (short_code,)
        )
        result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "Short URL not found"}), 404

    original_url = result[0]
    return redirect(original_url, code=302)




if __name__ == "__main__":
    app.run(debug=True)

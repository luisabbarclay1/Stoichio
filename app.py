"""
Stoichio – CS50 Final Project
Flask-based chemistry education website
"""

import sqlite3
from datetime import date
from flask import Flask, render_template, request, redirect, abort
import markdown

# Create Flask application
app = Flask(__name__)

# Helper function to connect to the SQLite database
def get_db():
    conn = sqlite3.connect("stoichio.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/what-to-avoid")
def what_to_avoid():
    return render_template("Weeklypoisons.html")

# Recently page:
# - GET displays the most recent posts
# - POST allows new posts to be added (future extension)

@app.route("/recently", methods=["GET", "POST"])
def recently():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        summary = request.form.get("summary", "").strip()
        body = request.form.get("body", "").strip()
        post_date = request.form.get("date", "").strip() or str(date.today())

        if title and summary:
            conn = get_db()
            conn.execute(
                "INSERT INTO posts (title, summary, date, body) VALUES (?, ?, ?, ?)",
                (title, summary, post_date, body),
            )
            conn.commit()
            conn.close()

        return redirect("/recently")

    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY date DESC, id DESC LIMIT 3"
    ).fetchall()
    conn.close()

    return render_template("recently.html", posts=posts)

# Archive page displaying all past posts
@app.route("/archive")
def archive():
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY date DESC, id DESC"
    ).fetchall()
    conn.close()

    return render_template("archive.html", posts=posts)

# Individual post page
@app.route("/post/<int:post_id>")
def post(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()

    if post is None:
        abort(404)

    body_html = markdown.markdown(post["body"], extensions=["tables"])

    return render_template("post.html", post=post, body_html=body_html)


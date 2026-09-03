import sqlite3

with open("article.md") as f:
    body = f.read()

conn = sqlite3.connect("stoichio.db")
conn.execute(
    "INSERT INTO posts (title, summary, date, body) VALUES (?, ?, ?, ?)",
    ("Retinoid Chemistry: Marketing Claims vs Molecular Reality",
     "Why the retinoid in your serum isn't the molecule that does the work, and what the evidence shows about whether that matters",
     "2026-09-03",
     body)
)
conn.commit()
conn.close()
print("Post inserted.")
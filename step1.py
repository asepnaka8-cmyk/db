import sqlite3
import re

def clean_text(text):
    if text is None:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'_+', '', text)
    return text.strip()

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute("SELECT id, content FROM page WHERE id IN (2, 3, 4)")
rows = cursor.fetchall()
data = {row[0]: clean_text(row[1]) for row in rows}

with open('input_bersih.txt', 'w', encoding='utf-8') as f:
    f.write("ID TARGET: 3\n")
    f.write("[TEKS SEBELUMNYA]: " + data.get(2, "") + "\n")
    f.write("[TEKS TARGET]: " + data.get(3, "") + "\n")
    f.write("[TEKS SETELAHNYA]: " + data.get(4, "") + "\n")

print("Step 1 done. Saved to input_bersih.txt")

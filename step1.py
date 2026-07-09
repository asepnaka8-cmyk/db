import sqlite3
import re

def clean_text(teks):
    if not teks: return ""
    # Hapus tag HTML
    teks = re.sub(r'<[^>]+>', '', teks)
    # Hapus garis bawah atau pemisah
    teks = re.sub(r'_+', '', teks)
    return teks.strip()

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

data = {}
for i in [3, 4, 5]:
    cursor.execute("SELECT content FROM page WHERE id = ?", (i,))
    row = cursor.fetchone()
    data[i] = clean_text(row[0]) if row else ""

conn.close()

output_text = f"""ID TARGET: 4
[TEKS SEBELUMNYA]: {data[3]}
[TEKS TARGET]: {data[4]}
[TEKS SETELAHNYA]: {data[5]}
"""

with open('input_bersih.txt', 'w', encoding='utf-8') as f:
    f.write(output_text)

print(output_text)

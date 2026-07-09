import sqlite3

def update_database():
    with open('irob_id_4.txt', 'r', encoding='utf-8') as f:
        analysis_content = f.read().strip()

    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE page
        SET analisis_lengkap = ?
        WHERE id = ?
    """, (analysis_content, 4))

    conn.commit()
    conn.close()
    print("Database updated successfully for id = 4.")

if __name__ == "__main__":
    update_database()

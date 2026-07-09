import sqlite3

def verify_update():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, LENGTH(analisis_lengkap) FROM page WHERE id = ?", (4,))
    row = cursor.fetchone()

    if row and row[1] and row[1] > 0:
        print(f"Verification successful. Record id={row[0]} has {row[1]} characters in analisis_lengkap.")
    else:
        print("Verification failed. The column might be empty or id not found.")

    conn.close()

if __name__ == "__main__":
    verify_update()

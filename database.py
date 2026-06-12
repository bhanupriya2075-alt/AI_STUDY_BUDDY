import sqlite3

conn = sqlite3.connect(
    "studybuddy.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature TEXT,
    input_text TEXT,
    output_text TEXT
)
""")

conn.commit()


def save_history(feature, input_text, output_text):

    cursor.execute(
        """
        INSERT INTO history
        (feature,input_text,output_text)
        VALUES (?,?,?)
        """,
        (feature, input_text, output_text)
    )

    conn.commit()


def get_history():

    cursor.execute(
        "SELECT * FROM history ORDER BY id DESC"
    )

    return cursor.fetchall()


def clear_history():

    cursor.execute(
        "DELETE FROM history"
    )

    conn.commit()
import sqlite3
import os

def create_db():
    try:
        if not os.access('.', os.W_OK):
            raise PermissionError('Current directory is not writable')
        
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS apps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                position TEXT NOT NULL,
                date_applied TEXT NOT NULL,
                job_url TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Database created successfully")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    create_db()



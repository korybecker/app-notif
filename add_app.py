import sqlite3
import sys
from datetime import datetime

def add_application(company, position, date_applied, job_url):
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO apps (company, position, date_applied, job_url)
        VALUES (?, ?, ?, ?)
    ''', (company, position, date_applied, job_url))
    conn.commit()
    conn.close()
    print(f"Application added for {company} - {position} on {date_applied}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: add_app.py <company> <position> <date_applied> <job_url>")
        sys.exit(1)

    company = sys.argv[1]
    position = sys.argv[2]
    date_applied = sys.argv[3]
    job_url = sys.argv[4]

    try:
        datetime.strptime(date_applied, '%Y-%m-%d')
    except ValueError:
        print("Date format should be YYYY-MM-DD")
        sys.exit(1)

    add_application(company, position, date_applied, job_url)


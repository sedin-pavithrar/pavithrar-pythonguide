from file_handler import FileHandler
from db_connection import database_connection
from pathlib import Path

BASE_DIR = Path(__file__).parent

file_path = BASE_DIR / "sample.txt"
db_path = BASE_DIR / "Employee.db"

print(f"Database: {db_path.resolve()}")

# ----------- File Handling ----------

with FileHandler(file_path, "w") as f:
    f.write("Hello from Pavi")

# ---------- Database Handling -------------

with database_connection(db_path) as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS department(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dept_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES department(id)
        )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO department(name) VALUES (?)",
        ("RF",)
    )

    cursor.execute(
        "INSERT OR IGNORE INTO department(name) VALUES (?)",
        ("HR",)
    )

    cursor.execute(
        "SELECT id FROM department WHERE name = ?",
        ("RF",)
    )
    rf_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT id FROM department WHERE name = ?",
        ("HR",)
    )
    hr_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO employee(name, dept_id) VALUES (?, ?)",
        ("Pavi", rf_id)
    )

    cursor.execute(
        "INSERT INTO employee(name, dept_id) VALUES (?, ?)",
        ("John", hr_id)
    )

    print("\nEmployee Details")

    cursor.execute("""
        SELECT
            e.id,
            e.name,
            d.name AS department
        FROM employee e
        INNER JOIN department d
            ON e.dept_id = d.id
    """)

    for emp_id, emp_name, dept_name in cursor.fetchall():
        print(f"ID: {emp_id}, Name: {emp_name}, Department: {dept_name}")

print("\nProgram Continues...")
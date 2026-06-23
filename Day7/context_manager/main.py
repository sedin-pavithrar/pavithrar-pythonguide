from file_handler import FileHandler
from db_connection import DbConnection
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

file_path = BASE_DIR / "sample.txt"
db_path = BASE_DIR / "Employee.db"
print()
print("Current Directory:", os.getcwd())
print()
print("Database Path:", os.path.abspath("Employee.db"))
print()
print(Path(__file__).parent)

with FileHandler(file_path,"w") as f:
    f.write("Hello from Pavi")


with DbConnection(db_path) as conn:
    cursor = conn.cursor()

    cursor.execute(""" 
CREATE TABLE IF NOT EXISTS employee(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT , dept TEXT
                   )
""")
    
    cursor.execute(
        "INSERT INTO employee(name , dept) VALUES (?,?)",
        ("Pavi","RF")
    )

    cursor.execute("SELECT * FROM employee")

    for row in cursor.fetchall():
        print(row)

print("Program Continues...")
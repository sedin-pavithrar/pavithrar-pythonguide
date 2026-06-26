import csv, glob
from pathlib import Path
def read_students(filepath): ...  # list of dicts
def calculate_grade(pct): ...    # "A+","A","B","C","F"
def write_results(students, out): ...
for fp in glob.glob("data/*.csv"):
    students=read_students(fp)
    write_results(students,f"results/{Path(fp).stem}_results.csv")
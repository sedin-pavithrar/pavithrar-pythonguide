Student CSV Report Generator
csv
DictReader
DictWriter
glob
pathlib
Real-world App
School ERP portals
Overview
Reads multiple student CSVs with csv.DictReader. Calculates total, percentage, and grade per 
student. Writes results with csv.DictWriter including a header row. glob.glob discovers all input files 
automatically. pathlib.Path.mkdir(exist_ok=True) creates the output folder if missing. This is how 
data ETL pipelines process batches of files.
Problem
Read student CSVs, calculate grades, write result CSVs. Use glob to batch-process all CSVs in 
a folder.
Starter Code
import csv, glob
from pathlib import Path
def read_students(filepath): ...  # list of dicts
def calculate_grade(pct): ...    # "A+","A","B","C","F"
def write_results(students, out): ...
for fp in glob.glob("data/*.csv"):
    students=read_students(fp)
    write_results(students,f"results/{Path(fp).stem}_results.csv")
    
CSV Format
# Input:  name,roll_no,maths,science,english,history,pe
# Output: name,roll_no,total,percentage,grade
Constraints
•  csv.DictReader and csv.DictWriter
•  glob.glob("data/*.csv") for multiple files
•  Path.mkdir for output folder if missing
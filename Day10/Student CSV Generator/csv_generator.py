import csv
import glob
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"

MAX_TOTAL = 500


def read_students(filepath: Path) -> list[dict]:
    """Read a student CSV and return a list of row dicts."""
    students = []

    with open(filepath, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def calculate_grade(percentage: float) -> str:
    """Return a letter grade for the given percentage (0–100)."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "F"


def write_results(students: list[dict], output_file: Path) -> None:
    """Calculate grades and write the result CSV."""

    RESULTS_DIR.mkdir(exist_ok=True)

    fieldnames = ["name", "roll_no", "total", "percentage", "grade"]

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            marks = [
                int(student["maths"]),
                int(student["science"]),
                int(student["english"]),
                int(student["history"]),
                int(student["pe"]),
            ]

            total = sum(marks)
            percentage = round((total / MAX_TOTAL) * 100, 2)
            grade = calculate_grade(percentage)

            writer.writerow(
                {
                    "name": student["name"],
                    "roll_no": student["roll_no"],
                    "total": total,
                    "percentage": percentage,
                    "grade": grade,
                }
            )


def main() -> None:

    csv_files = list(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in '{DATA_DIR}'.")
        return

    processed = 0

    for filepath in csv_files:
        students = read_students(filepath)

        if not students:
            print(f"Skipped '{filepath.name}' — no student data found.")
            continue

        output = RESULTS_DIR / f"{filepath.stem}_results.csv"
        write_results(students, output)

        print(f"Processed '{filepath.name}' -> '{output}' ({len(students)} student(s))")
        processed += 1

    print(f"\nDone. {processed} file(s) processed.")


if __name__ == "__main__":
    main()
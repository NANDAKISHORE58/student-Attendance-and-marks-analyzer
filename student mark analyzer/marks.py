import csv
import os


FILE = "data/marks.csv"


SUBJECTS = [
    "python",
    "dbms",
    "os",
    "cn"
]


def initialize_marks_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "python",
                "dbms",
                "os",
                "cn"
            ])


def get_marks():

    initialize_marks_file()

    records = []

    with open(FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def calculate_total(record):

    total = 0

    for subject in SUBJECTS:
        total += float(record[subject])

    return total


def calculate_average(record):

    total = calculate_total(record)

    return total / len(SUBJECTS)


def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def enter_marks():

    print("\n========== ENTER MARKS ==========")

    try:

        student_id = input("Enter Student ID: ").strip()

        marks = {}

        for subject in SUBJECTS:

            value = float(
                input(f"Enter {subject.upper()} marks: ")
            )

            if value < 0 or value > 100:

                print("Marks must be between 0 and 100.")
                return

            marks[subject] = value

        records = get_marks()

        found = False

        for record in records:

            if record["student_id"] == student_id:

                for subject in SUBJECTS:
                    record[subject] = str(marks[subject])

                found = True
                break

        if found:

            with open(FILE, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "student_id",
                        "python",
                        "dbms",
                        "os",
                        "cn"
                    ]
                )

                writer.writeheader()
                writer.writerows(records)

        else:

            with open(FILE, "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    student_id,
                    marks["python"],
                    marks["dbms"],
                    marks["os"],
                    marks["cn"]
                ])

        print("Marks recorded successfully!")

    except ValueError:

        print("Please enter valid marks.")


def view_marks():

    print("\n========== MARKS RECORDS ==========")

    records = get_marks()

    if not records:
        print("No marks records found.")
        return

    for record in records:

        total = calculate_total(record)
        average = calculate_average(record)
        grade = calculate_grade(average)

        print("--------------------------------")

        print("Student ID :", record["student_id"])

        print("Python :", record["python"])
        print("DBMS   :", record["dbms"])
        print("OS     :", record["os"])
        print("CN     :", record["cn"])

        print(f"Total   : {total:.2f}")
        print(f"Average : {average:.2f}")
        print(f"Grade   : {grade}")


def top_students():

    print("\n========== TOP STUDENTS ==========")

    records = get_marks()

    if not records:
        print("No marks records found.")
        return

    records.sort(
        key=lambda record: calculate_average(record),
        reverse=True
    )

    for index, record in enumerate(records[:3], start=1):

        average = calculate_average(record)

        print(
            f"{index}. Student ID: "
            f"{record['student_id']} "
            f"| Average: {average:.2f}"
        )


def pass_fail_analysis():

    print("\n========== PASS / FAIL ANALYSIS ==========")

    records = get_marks()

    if not records:
        print("No marks records found.")
        return

    for record in records:

        average = calculate_average(record)

        if average >= 50:
            status = "PASS"
        else:
            status = "FAIL"

        print(
            f"Student ID: {record['student_id']} "
            f"| Average: {average:.2f} "
            f"| {status}"
        )
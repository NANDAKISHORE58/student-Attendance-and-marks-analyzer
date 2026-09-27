import csv
import os


FILE = "data/attendance.csv"


def initialize_attendance_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "total_classes",
                "classes_attended"
            ])


def get_attendance():

    initialize_attendance_file()

    records = []

    with open(FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def calculate_percentage(total, attended):

    if total == 0:
        return 0

    return (attended / total) * 100


def record_attendance():

    print("\n========== RECORD ATTENDANCE ==========")

    try:

        student_id = input("Enter Student ID: ").strip()

        total_classes = int(
            input("Enter Total Classes: ")
        )

        classes_attended = int(
            input("Enter Classes Attended: ")
        )

        if total_classes <= 0:
            print("Total classes must be greater than zero.")
            return

        if classes_attended < 0 or classes_attended > total_classes:
            print("Invalid attendance values!")
            return

        records = get_attendance()

        found = False

        for record in records:

            if record["student_id"] == student_id:

                record["total_classes"] = str(total_classes)
                record["classes_attended"] = str(classes_attended)

                found = True
                break

        if found:

            with open(FILE, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "student_id",
                        "total_classes",
                        "classes_attended"
                    ]
                )

                writer.writeheader()
                writer.writerows(records)

        else:

            with open(FILE, "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    student_id,
                    total_classes,
                    classes_attended
                ])

        percentage = calculate_percentage(
            total_classes,
            classes_attended
        )

        print("Attendance recorded successfully!")
        print(f"Attendance Percentage: {percentage:.2f}%")

    except ValueError:

        print("Please enter valid numbers.")


def view_attendance():

    print("\n========== ATTENDANCE RECORDS ==========")

    records = get_attendance()

    if not records:
        print("No attendance records found.")
        return

    for record in records:

        total = int(record["total_classes"])
        attended = int(record["classes_attended"])

        percentage = calculate_percentage(
            total,
            attended
        )

        print("--------------------------------")

        print("Student ID :", record["student_id"])
        print("Total Classes :", total)
        print("Classes Attended :", attended)
        print(f"Attendance : {percentage:.2f}%")


def low_attendance_students():

    print("\n========== LOW ATTENDANCE ==========")

    records = get_attendance()

    found = False

    for record in records:

        total = int(record["total_classes"])
        attended = int(record["classes_attended"])

        percentage = calculate_percentage(
            total,
            attended
        )

        if percentage < 75:

            print(
                f"Student ID: {record['student_id']} "
                f"| Attendance: {percentage:.2f}%"
            )

            found = True

    if not found:
        print("No students below 75% attendance.")


def attendance_summary():

    print("\n========== ATTENDANCE SUMMARY ==========")

    records = get_attendance()

    if not records:
        print("No attendance records found.")
        return

    total_percentage = 0

    for record in records:

        total = int(record["total_classes"])
        attended = int(record["classes_attended"])

        percentage = calculate_percentage(
            total,
            attended
        )

        total_percentage += percentage

    average = total_percentage / len(records)

    print("Total Students:", len(records))
    print(f"Average Attendance: {average:.2f}%")
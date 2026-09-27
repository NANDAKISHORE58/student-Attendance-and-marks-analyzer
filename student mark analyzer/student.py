import csv
import os


FILE = "data/students.csv"


class Student:

    def __init__(self, student_id, name, department, section, year):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.section = section
        self.year = year

    def to_list(self):
        return [
            self.student_id,
            self.name,
            self.department,
            self.section,
            self.year
        ]


def initialize_student_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "department",
                "section",
                "year"
            ])


def get_students():

    initialize_student_file()

    students = []

    with open(FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def add_student():

    print("\n========== ADD STUDENT ==========")

    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        department = input("Enter Department: ").strip()
        section = input("Enter Section: ").strip()
        year = input("Enter Year: ").strip()

        if not student_id or not name or not department:
            print("Invalid student details!")
            return

        students = get_students()

        for student in students:

            if student["student_id"] == student_id:
                print("Student ID already exists!")
                return

        student = Student(
            student_id,
            name,
            department,
            section,
            year
        )

        with open(FILE, "a", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(student.to_list())

        print("Student added successfully!")

    except Exception as e:
        print("Error:", e)


def view_students():

    print("\n========== ALL STUDENTS ==========")

    students = get_students()

    if not students:
        print("No student records found.")
        return

    for student in students:

        print("--------------------------------")
        print("Student ID :", student["student_id"])
        print("Name       :", student["name"])
        print("Department :", student["department"])
        print("Section    :", student["section"])
        print("Year       :", student["year"])


def search_student():

    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    students = get_students()

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found")
            print("Student ID :", student["student_id"])
            print("Name       :", student["name"])
            print("Department :", student["department"])
            print("Section    :", student["section"])
            print("Year       :", student["year"])

            return

    print("Student not found!")


def update_student():

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    students = get_students()

    found = False

    for student in students:

        if student["student_id"] == student_id:

            print("Leave field blank to keep old value.")

            name = input(
                f"Enter new name ({student['name']}): "
            ).strip()

            department = input(
                f"Enter new department ({student['department']}): "
            ).strip()

            section = input(
                f"Enter new section ({student['section']}): "
            ).strip()

            year = input(
                f"Enter new year ({student['year']}): "
            ).strip()

            if name:
                student["name"] = name

            if department:
                student["department"] = department

            if section:
                student["section"] = section

            if year:
                student["year"] = year

            found = True
            break

    if not found:
        print("Student not found!")
        return

    with open(FILE, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "student_id",
                "name",
                "department",
                "section",
                "year"
            ]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Student updated successfully!")


def delete_student():

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    students = get_students()

    new_students = []

    found = False

    for student in students:

        if student["student_id"] == student_id:
            found = True
        else:
            new_students.append(student)

    if not found:
        print("Student not found!")
        return

    with open(FILE, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "student_id",
                "name",
                "department",
                "section",
                "year"
            ]
        )

        writer.writeheader()
        writer.writerows(new_students)

    print("Student deleted successfully!")
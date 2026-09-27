
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from attendance import (
    record_attendance,
    view_attendance,
    low_attendance_students,
    attendance_summary
)

from marks import (
    enter_marks,
    view_marks,
    top_students,
    pass_fail_analysis
)

from analyzer import (
    attendance_analysis,
    marks_analysis,
    grade_distribution,
    complete_analysis
)


# ==================================================
# STUDENT MANAGEMENT MENU
# ==================================================

def student_menu():

    while True:

        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


# ==================================================
# ATTENDANCE MANAGEMENT MENU
# ==================================================

def attendance_menu():

    while True:

        print("\n========== ATTENDANCE MANAGEMENT ==========")
        print("1. Record Attendance")
        print("2. View Attendance")
        print("3. Low Attendance Students")
        print("4. Attendance Summary")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            record_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            low_attendance_students()

        elif choice == "4":
            attendance_summary()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# ==================================================
# MARKS MANAGEMENT MENU
# ==================================================

def marks_menu():

    while True:

        print("\n========== MARKS MANAGEMENT ==========")
        print("1. Enter Marks")
        print("2. View Marks")
        print("3. Top Students")
        print("4. Pass / Fail Analysis")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_marks()

        elif choice == "2":
            view_marks()

        elif choice == "3":
            top_students()

        elif choice == "4":
            pass_fail_analysis()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# ==================================================
# ANALYSIS MENU
# ==================================================

def analysis_menu():

    while True:

        print("\n========== ANALYSIS ==========")
        print("1. Attendance Analysis")
        print("2. Marks Analysis")
        print("3. Grade Distribution")
        print("4. Complete Student Analysis")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            attendance_analysis()

        elif choice == "2":
            marks_analysis()

        elif choice == "3":
            grade_distribution()

        elif choice == "4":
            complete_analysis()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


# ==================================================
# MAIN MENU
# ==================================================

def main():

    while True:

        print("\n==============================================")
        print("   STUDENT ATTENDANCE AND MARKS ANALYZER")
        print("==============================================")

        print("1. Student Management")
        print("2. Attendance Management")
        print("3. Marks Management")
        print("4. Attendance Analysis")
        print("5. Marks Analysis")
        print("6. Complete Student Analysis")
        print("7. Grade Distribution")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            attendance_menu()

        elif choice == "3":
            marks_menu()

        elif choice == "4":
            attendance_analysis()

        elif choice == "5":
            marks_analysis()

        elif choice == "6":
            complete_analysis()

        elif choice == "7":
            grade_distribution()

        elif choice == "8":
            print("\nThank you for using Student Attendance and Marks Analyzer!")
            break

        else:
            print("Invalid choice! Please try again.")


# ==================================================
# PROGRAM START
# ==================================================

if __name__ == "__main__":
    main()


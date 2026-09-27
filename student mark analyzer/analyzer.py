import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from student import get_students
from attendance import get_attendance
from marks import get_marks


CHART_FOLDER = "charts"


# ==================================================
# HELPER FUNCTION
# ==================================================

def create_chart_folder():
    """Create charts folder if it does not exist."""
    os.makedirs(CHART_FOLDER, exist_ok=True)


# ==================================================
# ATTENDANCE ANALYSIS
# ==================================================

def attendance_analysis():

    print("\n========== ATTENDANCE ANALYSIS ==========")

    records = get_attendance()

    if not records:
        print("No attendance data available.")
        return

    df = pd.DataFrame(records)

    df["total_classes"] = pd.to_numeric(
        df["total_classes"]
    )

    df["classes_attended"] = pd.to_numeric(
        df["classes_attended"]
    )

    df["attendance_percentage"] = (
        df["classes_attended"] /
        df["total_classes"]
    ) * 100

    average = np.mean(
        df["attendance_percentage"]
    )

    highest = np.max(
        df["attendance_percentage"]
    )

    lowest = np.min(
        df["attendance_percentage"]
    )

    print(f"Average Attendance : {average:.2f}%")
    print(f"Highest Attendance : {highest:.2f}%")
    print(f"Lowest Attendance  : {lowest:.2f}%")

    print("\nStudents Below 75%:")

    low = df[
        df["attendance_percentage"] < 75
    ]

    if low.empty:
        print("None")
    else:
        print(
            low[
                [
                    "student_id",
                    "attendance_percentage"
                ]
            ].to_string(index=False)
        )

    # Create attendance chart
    create_chart_folder()

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["student_id"].astype(str),
        df["attendance_percentage"]
    )

    plt.axhline(
        y=75,
        linestyle="--",
        label="75% Requirement"
    )

    plt.xlabel("Student ID")
    plt.ylabel("Attendance Percentage")
    plt.title("Student Attendance Percentage")

    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            CHART_FOLDER,
            "attendance_chart.png"
        )
    )

    plt.show()

    print(
        "\nAttendance chart saved as "
        "charts/attendance_chart.png"
    )


# ==================================================
# MARKS ANALYSIS
# ==================================================

def marks_analysis():

    print("\n========== MARKS ANALYSIS ==========")

    records = get_marks()

    if not records:
        print("No marks data available.")
        return

    df = pd.DataFrame(records)

    subjects = [
        "python",
        "dbms",
        "os",
        "cn"
    ]

    for subject in subjects:

        df[subject] = pd.to_numeric(
            df[subject]
        )

    df["total"] = df[subjects].sum(axis=1)

    df["average"] = df[subjects].mean(axis=1)

    print(
        f"Class Average: "
        f"{np.mean(df['average']):.2f}"
    )

    print(
        f"Highest Average: "
        f"{np.max(df['average']):.2f}"
    )

    print(
        f"Lowest Average: "
        f"{np.min(df['average']):.2f}"
    )

    print("\nStudent Performance:")

    print(
        df[
            [
                "student_id",
                "total",
                "average"
            ]
        ].to_string(index=False)
    )

    # Create marks chart
    create_chart_folder()

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["student_id"].astype(str),
        df["average"]
    )

    plt.xlabel("Student ID")
    plt.ylabel("Average Marks")
    plt.title("Student Marks Comparison")

    plt.ylim(0, 100)
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            CHART_FOLDER,
            "marks_chart.png"
        )
    )

    plt.show()

    print(
        "\nMarks chart saved as "
        "charts/marks_chart.png"
    )


# ==================================================
# GRADE DISTRIBUTION
# ==================================================

def grade_distribution():

    print("\n========== GRADE DISTRIBUTION ==========")

    records = get_marks()

    if not records:
        print("No marks data available.")
        return

    df = pd.DataFrame(records)

    subjects = [
        "python",
        "dbms",
        "os",
        "cn"
    ]

    for subject in subjects:

        df[subject] = pd.to_numeric(
            df[subject]
        )

    df["average"] = df[subjects].mean(axis=1)

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

    df["grade"] = df["average"].apply(
        calculate_grade
    )

    grade_order = [
        "A+",
        "A",
        "B",
        "C",
        "D",
        "F"
    ]

    grade_counts = (
        df["grade"]
        .value_counts()
        .reindex(
            grade_order,
            fill_value=0
        )
    )

    print("\nGrade Distribution:")

    for grade, count in grade_counts.items():

        print(
            f"Grade {grade}: "
            f"{count} student(s)"
        )

    # Create grade chart
    create_chart_folder()

    plt.figure(figsize=(8, 6))

    plt.bar(
        grade_counts.index,
        grade_counts.values
    )

    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.title("Grade Distribution")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            CHART_FOLDER,
            "grade_chart.png"
        )
    )

    plt.show()

    print(
        "\nGrade chart saved as "
        "charts/grade_chart.png"
    )


# ==================================================
# COMPLETE STUDENT ANALYSIS
# ==================================================

def complete_analysis():

    print(
        "\n========== COMPLETE STUDENT ANALYSIS =========="
    )

    students = get_students()
    attendance = get_attendance()
    marks = get_marks()

    if not students:
        print("No student records found.")
        return

    student_df = pd.DataFrame(students)

    attendance_df = pd.DataFrame(
        attendance
    )

    marks_df = pd.DataFrame(
        marks
    )

    # ----------------------------------------------
    # Attendance Processing
    # ----------------------------------------------

    if not attendance_df.empty:

        attendance_df["total_classes"] = (
            pd.to_numeric(
                attendance_df["total_classes"]
            )
        )

        attendance_df["classes_attended"] = (
            pd.to_numeric(
                attendance_df["classes_attended"]
            )
        )

        attendance_df["attendance_percentage"] = (
            attendance_df["classes_attended"] /
            attendance_df["total_classes"]
        ) * 100

    # ----------------------------------------------
    # Marks Processing
    # ----------------------------------------------

    if not marks_df.empty:

        subjects = [
            "python",
            "dbms",
            "os",
            "cn"
        ]

        for subject in subjects:

            marks_df[subject] = pd.to_numeric(
                marks_df[subject]
            )

        marks_df["average"] = marks_df[
            subjects
        ].mean(axis=1)

    # ----------------------------------------------
    # Student Information
    # ----------------------------------------------

    result = student_df[
        [
            "student_id",
            "name",
            "department",
            "section"
        ]
    ]

    # ----------------------------------------------
    # Merge Attendance
    # ----------------------------------------------

    if not attendance_df.empty:

        result = result.merge(
            attendance_df[
                [
                    "student_id",
                    "attendance_percentage"
                ]
            ],
            on="student_id",
            how="left"
        )

    # ----------------------------------------------
    # Merge Marks
    # ----------------------------------------------

    if not marks_df.empty:

        result = result.merge(
            marks_df[
                [
                    "student_id",
                    "average"
                ]
            ],
            on="student_id",
            how="left"
        )

    print(
        result.to_string(index=False)
    )


# ==================================================
# END OF FILE
# ==================================================
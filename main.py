"""
main.py
Student Result & Grade Calculator

A simple command-line program that takes a student's marks in 5 subjects,
calculates the total, percentage, and grade, and stores the result so it
can be viewed or searched later.

Concepts used: variables, if-elif-else, operators (+, -, *, /, >=),
lists, dictionaries, loops, and basic file handling.
"""

RESULTS_FILE = "data/results.txt"

# students is a list of dictionaries, one dictionary per student
students = []


def load_students():
    """Load saved student results from the text file into the students list."""
    try:
        file = open(RESULTS_FILE, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            student = {
                "roll": parts[0],
                "name": parts[1],
                "marks": [int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6])],
                "total": int(parts[7]),
                "percentage": float(parts[8]),
                "grade": parts[9],
                "status": parts[10]
            }
            students.append(student)
        file.close()
    except FileNotFoundError:
        students.clear()


def save_students():
    """Write the students list back to the text file."""
    file = open(RESULTS_FILE, "w")
    for s in students:
        marks_str = str(s["marks"][0]) + "|" + str(s["marks"][1]) + "|" + str(s["marks"][2]) + "|" \
                    + str(s["marks"][3]) + "|" + str(s["marks"][4])
        line = (s["roll"] + "|" + s["name"] + "|" + marks_str + "|" + str(s["total"]) + "|"
                + str(s["percentage"]) + "|" + s["grade"] + "|" + s["status"] + "\n")
        file.write(line)
    file.close()


def calculate_grade(percentage):
    """Return a grade letter based on the percentage, using if-elif."""
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"
    return grade


def calculate_status(marks, percentage):
    """A student fails if overall percentage is below 40, or if any single
    subject is below 33 (common pass criteria used in many colleges)."""
    status = "Pass"

    if percentage < 40:
        status = "Fail"

    for mark in marks:
        if mark < 33:
            status = "Fail"

    return status


def add_student():
    print("\n--- Add Student Result ---")
    roll = input("Enter Roll Number: ").strip()

    if roll == "":
        print("Roll number cannot be empty.")
        return

    # check for duplicate roll number
    for s in students:
        if s["roll"] == roll:
            print("A student with this roll number already exists.")
            return

    name = input("Enter Student Name: ").strip()
    if name == "" or not name.replace(" ", "").isalpha():
        print("Invalid name! Please enter letters only.")
        return

    subjects = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]
    marks = []

    for subject in subjects:
        mark_input = input("Enter marks in " + subject + " (out of 100): ").strip()

        if not mark_input.isdigit():
            print("Invalid marks! Please enter a number.")
            return

        mark = int(mark_input)
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    # calculate total using the + operator
    total = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]

    # calculate percentage using the / and * operators
    percentage = (total / 500) * 100

    grade = calculate_grade(percentage)
    status = calculate_status(marks, percentage)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

    students.append(student)
    save_students()

    print("\nResult calculated successfully!")
    print("Total Marks   :", total, "/ 500")
    print("Percentage    :", round(percentage, 2), "%")
    print("Grade         :", grade)
    print("Status        :", status)


def view_all_students():
    print("\n--- All Student Results ---")
    if len(students) == 0:
        print("No results found yet.")
        return

    for s in students:
        print("Roll:", s["roll"], "| Name:", s["name"], "| Total:", s["total"],
              "/500 | %:", round(s["percentage"], 2), "| Grade:", s["grade"],
              "| Status:", s["status"])


def search_student():
    print("\n--- Search Student by Roll Number ---")
    roll = input("Enter Roll Number: ").strip()

    for s in students:
        if s["roll"] == roll:
            print("\nRoll Number  :", s["roll"])
            print("Name         :", s["name"])
            print("Marks        :", s["marks"])
            print("Total        :", s["total"], "/ 500")
            print("Percentage   :", round(s["percentage"], 2), "%")
            print("Grade        :", s["grade"])
            print("Status       :", s["status"])
            return

    print("No student found with that roll number.")


def class_summary():
    """Simple analytics: how many passed, failed, and the class average."""
    print("\n--- Class Summary ---")
    if len(students) == 0:
        print("No results found yet.")
        return

    total_students = len(students)
    passed = 0
    failed = 0
    percentage_sum = 0

    for s in students:
        if s["status"] == "Pass":
            passed = passed + 1
        else:
            failed = failed + 1
        percentage_sum = percentage_sum + s["percentage"]

    class_average = percentage_sum / total_students

    print("Total Students :", total_students)
    print("Passed         :", passed)
    print("Failed         :", failed)
    print("Class Average  :", round(class_average, 2), "%")


def main():
    load_students()

    while True:
        print("\n========================================")
        print("     STUDENT RESULT & GRADE CALCULATOR")
        print("========================================")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Search Student by Roll Number")
        print("4. View Class Summary")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            print("Thank you for using the Student Result Calculator!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()

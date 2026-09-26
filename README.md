# Student Result & Grade Calculator

A simple Python command-line program that calculates a student's total
marks, percentage, grade, and pass/fail status, and keeps a record of
all students entered.

## Overview

Teachers often calculate results by hand — adding up marks, dividing by
the total, and deciding the grade using fixed percentage ranges. This
program automates that process and also keeps a record of every
student's result for later reference.

## Features

- **Add Student Result** — enter a student's roll number, name, and
  marks in 5 subjects; the program calculates total, percentage,
  grade, and pass/fail status automatically
- **View All Results** — see every student's result in one list
- **Search Student by Roll Number** — look up one student's full
  result
- **View Class Summary** — see how many students passed/failed and the
  class average percentage

## Technologies Used

- Python 3 (only built-in features, no external libraries)
- `if-elif-else` statements to decide the grade and pass/fail status
- Arithmetic operators (`+`, `/`, `*`) to calculate total and percentage
- A list to hold each subject's marks, and a list of dictionaries to
  hold all student records
- A plain text file (`data/results.txt`) to save results permanently

## Project Structure

```
student_result/
├── main.py           # the whole program
└── data/
    └── results.txt    # saved student results (created automatically)
```

## How It Works

- Each student is stored as a dictionary with roll number, name, a
  list of 5 marks, total, percentage, grade, and status.
- `calculate_grade()` uses an `if-elif` ladder to turn a percentage
  into a letter grade (A+, A, B, C, D, E, F).
- `calculate_status()` checks two conditions using `if`: whether the
  overall percentage is below 40, and whether any single subject is
  below 33 — either one results in a "Fail".
- Results are saved to `data/results.txt` so they are not lost when
  the program closes.

## Steps to Install & Run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Open this folder in a terminal or VS Code.
3. Run the program:
   ```
   python main.py
   ```

## How to Test It

1. Choose **1** and enter a roll number, name, and marks for 5 subjects
   (try marks that would give an "A" grade, e.g. 85, 78, 92, 88, 95).
2. Choose **1** again and add a second student with one subject below
   33 (e.g. 30, 45, 50, 40, 38) to see the "Fail" status trigger even
   though the overall percentage looks okay.
3. Choose **2** to view both results together.
4. Choose **3** and search using the first student's roll number.
5. Choose **4** to see the class average and pass/fail count.

## Non-Functional Points Covered

- **Validation** — marks must be a number between 0 and 100; name must
  be letters only; duplicate roll numbers are rejected
- **Error Handling** — invalid input shows a message instead of
  crashing the program
- **Data Persistence** — results are saved in a text file so they are
  remembered next time the program runs
- **Usability** — a short numbered menu guides the user through every
  option

## Challenges Faced

- Deciding the exact percentage ranges for each grade using `if-elif`
- Handling the case where a student fails one subject but still has a
  passing overall percentage
- Making sure duplicate roll numbers are not added twice

## Future Enhancements

- Allow a configurable number of subjects instead of a fixed 5
- Export results to a formatted report card (PDF)
- Add rank calculation among all students

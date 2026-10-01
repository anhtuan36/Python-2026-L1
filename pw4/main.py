
import os
import curses
import numpy as np

import pw4.input as in_mod
import pw4.output as out_mod


def calculate_gpas(students, courses, marks):
    for s in students:
        marks_list = []
        credits_list = []

        for c in courses:
            cid = c.get_id()
            if cid in marks and s.get_id() in marks[cid]:
                marks_list.append(marks[cid][s.get_id()])
                credits_list.append(c.get_credits())

        if marks_list and sum(credits_list) > 0:
            # Weighted GPA using NumPy arrays
            np_marks = np.array(marks_list, dtype=float)
            np_credits = np.array(credits_list, dtype=float)
            weighted_gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            s.set_gpa(round(float(weighted_gpa), 2))
        else:
            s.set_gpa(0.0)


def run_system(stdscr):
    # 1. Inputs
    students = in_mod.input_students(stdscr)
    courses = in_mod.input_courses(stdscr)
    marks = in_mod.input_marks(stdscr, students, courses)

    # 2. GPA Calculation & Ranking
    calculate_gpas(students, courses, marks)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)

    # 3. Output
    out_mod.display_rankings(stdscr, students)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    curses.wrapper(run_system)
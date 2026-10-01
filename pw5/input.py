
import curses
import math
from pw5.domains import Student, Course


def read_text(win, y, x, prompt):
    try:
        win.addstr(y, x, prompt)
    except curses.error:
        pass
    win.clrtoeol()
    curses.echo()
    curses.curs_set(1)
    val = win.getstr(y, x + len(prompt)).decode("utf-8").strip()
    curses.noecho()
    curses.curs_set(0)
    return val


def input_students(stdscr):
    students = []
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 1: STUDENT INPUT ===", curses.A_BOLD)
    num_students = int(read_text(stdscr, 3, 2, "Enter number of students: "))

    for i in range(num_students):
        stdscr.clear()
        stdscr.addstr(1, 2, f"=== STUDENT {i + 1}/{num_students} ===", curses.A_BOLD)
        sid = read_text(stdscr, 3, 4, "Student ID: ")
        name = read_text(stdscr, 4, 4, "Student Name: ")
        dob = read_text(stdscr, 5, 4, "DoB (DD/MM/YYYY): ")
        students.append(Student(sid, name, dob))

    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()}|{s.get_name()}|{s.get_dob()}\n")

    return students


def input_courses(stdscr):
    courses = []
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 2: COURSE INPUT ===", curses.A_BOLD)
    num_courses = int(read_text(stdscr, 3, 2, "Enter number of courses: "))

    for i in range(num_courses):
        stdscr.clear()
        stdscr.addstr(1, 2, f"=== COURSE {i + 1}/{num_courses} ===", curses.A_BOLD)
        cid = read_text(stdscr, 3, 4, "Course ID: ")
        cname = read_text(stdscr, 4, 4, "Course Name: ")
        credits = int(read_text(stdscr, 5, 4, "Credits: "))
        courses.append(Course(cid, cname, credits))

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()}|{c.get_name()}|{c.get_credits()}\n")

    return courses


def input_marks(stdscr, students, courses):
    marks = {}

    for c in courses:
        cid = c.get_id()
        marks[cid] = {}
        stdscr.clear()
        stdscr.addstr(1, 2, f"=== MARKS FOR: {c.get_name()} ({cid}) ===", curses.A_BOLD)

        row = 3
        for s in students:
            raw_val = float(read_text(stdscr, row, 4, f"Mark for {s.get_name()}: "))
            floored = math.floor(raw_val * 10) / 10.0
            marks[cid][s.get_id()] = floored
            row += 1

    with open("marks.txt", "w", encoding="utf-8") as f:
        for cid, student_dict in marks.items():
            for sid, score in student_dict.items():
                f.write(f"{cid}|{sid}|{score}\n")

    return marks
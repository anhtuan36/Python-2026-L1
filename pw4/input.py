
import curses
import math
from pw4.domains import Student, Course


def read_text(win, y, x, prompt):
    win.addstr(y, x, prompt)
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

    row = 5
    for i in range(num_students):
        stdscr.addstr(row, 2, f"Student {i + 1}:", curses.A_UNDERLINE)
        sid = read_text(stdscr, row + 1, 4, "Student ID: ")
        name = read_text(stdscr, row + 2, 4, "Student Name: ")
        dob = read_text(stdscr, row + 3, 4, "DoB (DD/MM/YYYY): ")
        students.append(Student(sid, name, dob))
        row += 5

    return students


def input_courses(stdscr):
    courses = []
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 2: COURSE INPUT ===", curses.A_BOLD)
    num_courses = int(read_text(stdscr, 3, 2, "Enter number of courses: "))

    row = 5
    for i in range(num_courses):
        stdscr.addstr(row, 2, f"Course {i + 1}:", curses.A_UNDERLINE)
        cid = read_text(stdscr, row + 1, 4, "Course ID: ")
        cname = read_text(stdscr, row + 2, 4, "Course Name: ")
        credits = int(read_text(stdscr, row + 3, 4, "Credits: "))
        courses.append(Course(cid, cname, credits))
        row += 5

    return courses


def input_marks(stdscr, students, courses):
    marks = {}  # {cid: {sid: mark}}
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 3: MARK INPUT (Floored to 1 decimal) ===", curses.A_BOLD)

    row = 3
    for c in courses:
        cid = c.get_id()
        marks[cid] = {}
        stdscr.addstr(row, 2, f"Course: {c.get_name()} ({cid})", curses.A_BOLD)
        row += 1

        for s in students:
            raw_val = float(read_text(stdscr, row, 4, f"Mark for {s.get_name()}: "))
            # Floor down to 1 decimal place using math.floor
            floored_val = math.floor(raw_val * 10) / 10.0
            marks[cid][s.get_id()] = floored_val
            row += 1
        row += 1

    return marks
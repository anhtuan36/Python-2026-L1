
import curses
import math
import numpy as np


class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f"{self.__id:<10} | {self.__name:<20} | {self.__dob:<12} | GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, cid="", name="", credits=0):
        self.__id = cid
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__id:<10} | {self.__name:<25} | Credits: {self.__credits}"


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  # {course_id: {student_id: mark}}

    def add_student(self, sid, name, dob):
        self.students.append(Student(sid, name, dob))

    def add_course(self, cid, name, credits):
        self.courses.append(Course(cid, name, credits))

    def set_mark(self, cid, sid, raw_mark):
        # Round-down to 1 decimal place using math.floor
        rounded = math.floor(float(raw_mark) * 10) / 10.0
        if cid not in self.marks:
            self.marks[cid] = {}
        self.marks[cid][sid] = rounded

    def calculate_gpas(self):
        for s in self.students:
            marks_list = []
            credits_list = []

            for c in self.courses:
                cid = c.get_id()
                if cid in self.marks and s.get_id() in self.marks[cid]:
                    marks_list.append(self.marks[cid][s.get_id()])
                    credits_list.append(c.get_credits())

            if marks_list and sum(credits_list) > 0:
                # Weighted average calculation via NumPy arrays
                np_marks = np.array(marks_list, dtype=float)
                np_credits = np.array(credits_list, dtype=float)
                gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
                s.set_gpa(round(float(gpa), 2))
            else:
                s.set_gpa(0.0)

    def sort_students_by_gpa(self):
        self.calculate_gpas()
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)


# --- Curses Helper Functions ---

def read_input(win, y, x, prompt):
    win.addstr(y, x, prompt)
    win.clrtoeol()
    curses.echo()
    curses.curs_set(1)
    val = win.getstr(y, x + len(prompt)).decode("utf-8").strip()
    curses.noecho()
    curses.curs_set(0)
    return val


def main(stdscr):
    system = SchoolSystem()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # 1. Input Students
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 1: STUDENT INPUT ===", curses.color_pair(1) | curses.A_BOLD)
    num_students = int(read_input(stdscr, 3, 2, "Enter number of students: "))
    
    current_row = 5
    for i in range(num_students):
        stdscr.addstr(current_row, 2, f"Student {i + 1}:", curses.A_UNDERLINE)
        sid = read_input(stdscr, current_row + 1, 4, "Student ID: ")
        name = read_input(stdscr, current_row + 2, 4, "Student Name: ")
        dob = read_input(stdscr, current_row + 3, 4, "DoB (DD/MM/YYYY): ")
        system.add_student(sid, name, dob)
        current_row += 5

    # 2. Input Courses
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 2: COURSE INPUT ===", curses.color_pair(1) | curses.A_BOLD)
    num_courses = int(read_input(stdscr, 3, 2, "Enter number of courses: "))
    
    current_row = 5
    for i in range(num_courses):
        stdscr.addstr(current_row, 2, f"Course {i + 1}:", curses.A_UNDERLINE)
        cid = read_input(stdscr, current_row + 1, 4, "Course ID: ")
        cname = read_input(stdscr, current_row + 2, 4, "Course Name: ")
        credits = int(read_input(stdscr, current_row + 3, 4, "Credits: "))
        system.add_course(cid, cname, credits)
        current_row += 5

    # 3. Input Marks
    stdscr.clear()
    stdscr.addstr(1, 2, "=== STEP 3: MARK INPUT (Floored to 1 decimal) ===", curses.color_pair(1) | curses.A_BOLD)
    current_row = 3
    for c in system.courses:
        stdscr.addstr(current_row, 2, f"Course: {c.get_name()} ({c.get_id()})", curses.color_pair(3) | curses.A_BOLD)
        current_row += 1
        for s in system.students:
            val = float(read_input(stdscr, current_row, 4, f"Mark for {s.get_name()}: "))
            system.set_mark(c.get_id(), s.get_id(), val)
            current_row += 1
        current_row += 1

    # 4. Sort and Display Ranking
    system.sort_students_by_gpa()

    stdscr.clear()
    stdscr.addstr(1, 2, "=== STUDENT RANKING BY GPA (DESCENDING) ===", curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(3, 2, f"{'Rank':<5} {'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<5}")
    stdscr.addstr(4, 2, "-" * 60)

    line = 5
    for rank, s in enumerate(system.students, start=1):
        stdscr.addstr(line, 2, f"{rank:<5} {s}")
        line += 1

    stdscr.addstr(line + 2, 2, "Press any key to exit...", curses.A_DIM)
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
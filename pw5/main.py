
import os
import sys
from pathlib import Path
import zipfile
import curses
import numpy as np

sys.path.append(str(Path(__file__).resolve().parent))

from pw5.domains import Student, Course
import pw5.input as in_mod
import pw5.output as out_mod

ARCHIVE_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]


def decompress_archive():
    if os.path.exists(ARCHIVE_FILE):
        with zipfile.ZipFile(ARCHIVE_FILE, "r") as archive:
            archive.extractall(".")
        return True
    return False


def load_persistent_data():
    students = []
    courses = []
    marks = {}

    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    cid, sid, score = parts[0], parts[1], float(parts[2])
                    if cid not in marks:
                        marks[cid] = {}
                    marks[cid][sid] = score

    for fname in TXT_FILES:
        if os.path.exists(fname):
            os.remove(fname)

    return students, courses, marks


def compress_archive():
    with zipfile.ZipFile(ARCHIVE_FILE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for fname in TXT_FILES:
            if os.path.exists(fname):
                archive.write(fname)
                os.remove(fname)


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
            np_marks = np.array(marks_list, dtype=float)
            np_credits = np.array(credits_list, dtype=float)
            weighted_gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            s.set_gpa(round(float(weighted_gpa), 2))
        else:
            s.set_gpa(0.0)


def run_system(stdscr):
    if decompress_archive():
        students, courses, marks = load_persistent_data()
        source_label = "Loaded from students.dat"
    else:
        students = in_mod.input_students(stdscr)
        courses = in_mod.input_courses(stdscr)
        marks = in_mod.input_marks(stdscr, students, courses)
        source_label = "Manual Input"
        compress_archive()

    calculate_gpas(students, courses, marks)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)

    out_mod.display_rankings(stdscr, students, source_label)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    curses.wrapper(run_system)
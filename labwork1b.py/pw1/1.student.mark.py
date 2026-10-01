
student = []
course = []
mark = {} #format: {course_id: {student_id: mark}}

    # Students

def input_students():
    numstudent = int(input("Enter the number of student: "))
    for i in range(numstudent):
        sname = input("Student name: ")
        sid = input("Student ID: ")
        sdob = input("Date of birth: ")
        student.append({"name": sname, "id": sid, "dob": sdob})

    # Courses

def input_courses():
    numcorse = int(input("Enter the number of courses: "))
    for i in range(numcorse):
        cname = input("Course name: ")
        cid = input("Course ID: ")
        course.append({"name": cname, "id": cid})

    # Marks

def input_marks():
    cid = input("\nEnter Course ID to input Marks: ")
    mark[cid] = {}
    for s in student:
        mark[cid][s["id"]] = float(input(f"Mark for {s['name']}: "))

    # Display

def list_students():
    print("\n   Student list   ")
    for s in student:
        print(s["id"], s["name"], s["dob"])

def list_courses():
    print("\n   Course list   ")
    for c in course:
        print(c["id"], c["name"])

def show_marks():
    cid = input("\nEnter Course ID to view marks: ")
    print(f"   Marks for course {cid}   ")
    for s in student:
        print(s["name"], ":", mark.get(cid, {}).get(s["id"], "Not Available"))

    
input_students()
input_courses()
input_marks()
list_students()
list_courses()
show_marks()

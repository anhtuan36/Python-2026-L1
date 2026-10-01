
class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__id = sid
        self.__name = name
        self.__dob = dob

    # Getters (Encapsulation)
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Polymorphic input method
    def input(self):
        self.__name = input("Student name: ")
        self.__id = input("Student ID: ")
        self.__dob = input("Date of birth: ")

    # Polymorphic display method
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")

    def __str__(self):
        return f"{self.__id} - {self.__name} ({self.__dob})"


class Course:
    def __init__(self, cid="", name=""):
        self.__id = cid
        self.__name = name

    # Getters (Encapsulation)
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    # Polymorphic input method
    def input(self):
        self.__name = input("Course name: ")
        self.__id = input("Course ID: ")

    # Polymorphic display method
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name}")

    def __str__(self):
        return f"{self.__id} - {self.__name}"


class SchoolSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # {course_id: {student_id: mark}}

    # Student management
    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            s = Student()
            s.input()
            self.__students.append(s)

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.__students:
            s.list()

    # Course management
    def input_courses(self):
        num_courses = int(input("\nEnter the number of courses: "))
        for _ in range(num_courses):
            c = Course()
            c.input()
            self.__courses.append(c)

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.__courses:
            c.list()

    # Mark management
    def input_marks(self):
        cid = input("\nEnter Course ID to input marks: ")
        # Verify if course exists
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            print("Course ID not found!")
            return

        if cid not in self.__marks:
            self.__marks[cid] = {}

        print(f"Entering marks for {course.get_name()}:")
        for s in self.__students:
            mark = float(input(f"Mark for {s.get_name()}: "))
            self.__marks[cid][s.get_id()] = mark

    def show_marks(self):
        cid = input("\nEnter Course ID to view marks: ")
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            print("Course ID not found!")
            return

        print(f"\n--- Marks for Course: {course.get_name()} ({cid}) ---")
        for s in self.__students:
            mark = self.__marks.get(cid, {}).get(s.get_id(), "Not Available")
            print(f"{s.get_name()}: {mark}")


# Main execution
if __name__ == "__main__":
    system = SchoolSystem()
    
    system.input_students()
    system.input_courses()
    system.input_marks()
    
    system.list_students()
    system.list_courses()
    system.show_marks()
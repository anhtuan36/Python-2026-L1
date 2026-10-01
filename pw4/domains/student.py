
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

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
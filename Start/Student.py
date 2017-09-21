class Student:
    __name = None
    __department = None
    __grade = None

    # def __init__(self, name):
    #     self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    def __str__(self) -> str:
        # return "Name - %s, Department - %s, Grade - %s" % (self.__name, self.__department, self.__grade)
        return "Name - {}, Department - {}, Grade - {}".format(self.__name, self.__department, self.__grade)

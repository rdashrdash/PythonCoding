class Student:
    def __init__(self):
        self.name = "Vir"
        self.grades = (45, 85, 96, 72)

    def average(self):
        return sum(self.grades)/ len(self.grades)


student = Student()
# print(student.name)
# print(Student.grades)
# print(Student.average(student))
print(student.average())


class Studs:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades)/ len(self.grades)


student1 = Studs("Yol", (45, 52, 98, 67))
student2 = Studs("Poi", (85, 42, 48, 97))
print(student1.name)
print(student1.average_grade())
print(student2.average_grade())
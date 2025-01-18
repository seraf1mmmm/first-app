class Student:
    amount = 0
    height = 120
    def __init__ (self, height = 160, name = None, age):
        self.height = height
        self.name = name
        self.age = age
        Student.amount += 1

    def __bool__ (self):
        return self.name != None

    def __len__(self):
        return self.height

    def printer(self):
        print(self.height, self.name, self. age)

    def __str__(self):
        return f"i am a student. My name is {self.name}"

first_student = Student(160, "antonchik", 15)
second_student = Student(170, "Vlad", 14)
maximka_student = Student(170, "Maximka", 14)
print(first_student.height, first_student.name, first_student.age, "amount =", Student.amount)
print(second_student.height, second_student.name, second_student.age, "amount =", Student.amount)

first_student.printer()
second_student.printer()
maximka_student.printer()
print(first_student)

nick = Student()
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))
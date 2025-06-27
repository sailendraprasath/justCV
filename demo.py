class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)

stud = Student("Sailesh",20,7.2)
stud.display()
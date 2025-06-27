class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)

student_record = []
num = int(input("Enter the number of students: "))

for val in range(num):
    name = input("Enter the name of student: ")
    age = int(input("Enter the age of student: "))
    grade = float(input("Enter the grade of student: "))
    student = Student(name, age, grade)
    student_record.append(student)

for student in student_record:
    student.display()
    print("----------")
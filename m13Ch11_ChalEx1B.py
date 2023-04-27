
# m13 Ch11 Inheritance class ex 10
# project #1

class person:
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name 
        self.age = age
        self.address = address 
        self.city = city
        self.state = state 
        self.zipcode = zipcode

# the student class is inheriting from the person class
class Student(person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):

        name = input('enter the name ')
        age = input('enter the age ')
        address = input('enter the address ')
        city = input('enter the city ')
        state = input('enter the state ')
        zipcode = input('enter the zipcode ')
        studentID = input('enter the Student ID ')
        GPA = input('enter the GPA ')        

        # The super keyword is calling the super class
        # which is the person class and passing name, and age

        super().__init__(name, age, address, city, state, zipcode)

        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, address, city, state, zipcode,TeacherID, ClassTeaching):
        super().__init__(name,age, address, city, state, zipcode)

        name = input('enter the name ')
        age = input('enter the age ')
        address = input('enter the address ')
        city = input('enter the city ')
        state = input('enter the state ')
        zipcode = input('enter the zipcode ')
        TeacherID = input('enter the Teacher ID ')
        ClassTeaching = input('enter the name of the course teaching ')        

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('Jane Doe', 25, '543 Melborn Ave', 'BayStray', 'LA', '70005', 777, 3.8)
print('Student Name: ', student.name)
print('Student age: ', student.age)
print('Student address: ', student.address)
print('Student city: ', student.city)
print('Student state: ', student.state)
print('Student zipcode: ', student.zipcode)
print('Student ID: ', student.studentID)
print('Student GPA: ', student.GPA)

print('\n')

teacher = Teacher('Ms. Cantor', 45, '123 Abc St', 'Santa Ana', 'CA', '93888', 7, 'Python')
print('Teacher Name: ', teacher.name)
print('Teacher Age: ', teacher.age)
print('Teacher address: ', teacher.address)
print('Teacher city: ', teacher.city)
print('Teacher state: ', teacher.state)
print('Teacher zipcode: ', teacher.zipcode)
print('Teacher ID: ', teacher.TeacherID)
print('Teacher Course: ', teacher.ClassTeaching)
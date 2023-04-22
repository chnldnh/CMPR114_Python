
# m9Ch10ClassEx9_ChalEx2

class Teacher:
    # using init to create a customized constructor
    # here we have three arguments
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print("Professor name is " + self.name)
        print("Professor assigned class is " + self.classRoom)
        print("Professor is teaching " + self.course)

Teacher1 = Teacher("Prof.Sim", "A206", "Python Programming")
Teacher1.GetProfessor()
print()
# create 2nd object
Teacher2 = Teacher("Dr. Sourze", "B100", "Python Programming II")
Teacher2.GetProfessor()

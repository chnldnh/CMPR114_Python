
# m9Ch10ClassEx9_ChalEx1

class Students:
    # the keyword (self) it is used to access variables that belong to that class
    def GetInformation(self):
        print("student Lastname name is " + self.Lastname)
        print("student Firstname name is " + self.Firstname)
        print("student Address name is " + self.Address)
        print("student City name is " + self.City)
        print("student State name is " + self.State)
        print("student Zipcode name is " + self.Zipcode)        

        self.lastname = input("Student3 Lastname is ")
        self.firstName = input("Student3 Firstname is ") 
        self.address = input("Student3 Address is ")
        self.city = input("Student3 City is ")
        self.state = input("Student3 State is ")
        self.zipcode = input("Student3 Zipcode is ")       
       
    #def PrintStudent3(self):         # Student3    
    #    self.lastname = input("Student3 Lastname is ")
    #    self.firstName = input("Student3 Firstname is ") 
    #    self.address = input("Student3 Address is ")
    #    self.city = input("Student3 City is ")
    #    self.state = input("Student3 State is ")
    #    self.zipcode = input("Student3 Zipcode is ")       

# create the Student1 object
Student1 = Students()
Student1.Lastname = "Doe" 
Student1.Firstname = "Jane" 
Student1.Address = "111 St" 
Student1.City = "Santa Ana" 
Student1.State = "CA" 
Student1.Zipcode = "12345\n" 

# create the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor" 
Student2.Firstname = "Mike" 
Student2.Address = "222 St" 
Student2.City = "Garden Grove" 
Student2.State = "CA" 
Student2.Zipcode = "67890\n" 

Student3 = Students()  

# Calling the funciton
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
#Student3.PrintStudent3()


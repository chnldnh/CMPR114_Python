
# m13 Ch11 Inheritance + class ex #10
# Challenge Ex #7
import sys
class Employee:   
    def __init__(self, empName, empNum):
        self.__empName = empName
        self.__empNum = empNum

    def get_empName(self): # Create accessor method for __empName attribute
        return self.__empName

    def set_empName(self, empName): # Create mutator method for __empName attribute
        self.__empName = empName

    def get_empNum(self): # Create accessor method for __empNum attribute
        return self.__empNum

    def set_empNum(self, empNum): # Create mutator method for __empNum attribute
        self.__empNum = empNum

class ShiftSupervisor(Employee):
    def __init__(self, empName, empNum, shiftNum, payRate, annualSal, annualBon):  
        Employee.__init__(self, empName, empNum) # Call the superclass's __init__ method and pass arguments.

        # Inititalize the __shiftNum attribute.
        self.__shiftNum = shiftNum

         # Inititalize the __payRate attribute.
        self.__payRate = payRate
       
        self.__annualSal = annualSal
       
        self.__annualBon = annualBon
    def get_shiftNum(self): # Create accessor method for __shiftNum attribute  
        if self.__shiftNum == 1:  
            s = 'Day'
        elif self.__shiftNum == 2:
            s = 'Night'
        elif self.__shiftNum == 3:
            s = 'Night'
        return s       

    def set_shiftNum(self, shiftNum): # Create mutator method for __shiftNum attribute            
         self.__shiftNum = shiftNum

    def get_payRate(self): # Create accessor method for __payRate attribute
        return self.__payRate

    def set_payRate(self, payRate): # Create mutator method for __payRate attribute
        self.__payRate = payRate

    def get_annualSal(self): # Create accessor method for __salary attribute       
        return  self.__annualSal 

    def set_annualSal(self, annualSal): # Create mutator method for __salary attribute          
         self.__annualSal = annualSal

    def get_annualBon(self):       
        return self.__annualBon

    def set_annualBon(self, annualBon):        
        self.__annualBon = annualBon


        
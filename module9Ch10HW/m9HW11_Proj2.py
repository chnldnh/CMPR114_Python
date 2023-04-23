
# m9HW11_Proj2
# Employee Class

class Employee:
    def __init__(self, name, idNum, dept, jobTitle):
        self.__name = name
        self.__idNum = idNum
        self.__dept = dept
        self.__jobTitle = jobTitle

    def getName(self):
        return self.__name

    def getidNum(self):
        return self.__idNum

    def getDept(self):
        return self.__dept

    def getJobTitle(self):
        return self.__jobTitle

    def setName(self, name):
        self.name = name

    def setidNum(self, idNum):
        self.idNum = idNum

    def setDept(self, dept):
        self.dept = dept

    def setJobTitle(self, jobTitle):
        self.jobTitle = jobTitle
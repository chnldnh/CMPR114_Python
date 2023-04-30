# m13 homework #13
# Project #2

class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, cusNum, mailList):
        Person.__init__(self, name, address, phone)
        self.__cusNum = cusNum
        self.__mailList = mailList

    def get_cusNum(self):
        return self.__cusNum

    def set_cusNum(self, cusNum):
        self.__cusNum = cusNum

    def get_mailList(self):
        self.__mailList = mailList

    def set_mailList(self, mailList):
        self.__mailList = mailList.lower()
        if self.__mailList == 'y':
            a = 'You are on the mailing list.'
        elif self.__mailList == 'n':
            a = 'You are not on the mailing list.'
        else:
            a = 'Error! Enter y or n'
        return a
   
        




# m9Ch10ClassEx9_ChalEx3

class PI:
    #passing 3 parameters
    def GetInformation(self, LN, FN, Age, address, city, state, zipcode):
        return LN + " , " + FN + " , " + str(Age) + " \n" + address + " \n" + city + " , " + state + " , " + zipcode 

PersonalInformation = PI()
PersonalInformation.Lastname = input('enter the lastname ')
PersonalInformation.Firstname = input('enter the firstname ')
PersonalInformation.Age = int(input('enter the age '))
PersonalInformation.Address = input('enter the address ')
PersonalInformation.City = input('enter the city ')
PersonalInformation.State = input('enter the state ')
PersonalInformation.Zipcode = input('enter the zipcode ')

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, 
                                         PersonalInformation.Firstname, PersonalInformation.Age, 
                                         PersonalInformation.Address, PersonalInformation.City, 
                                         PersonalInformation.State, PersonalInformation.Zipcode))


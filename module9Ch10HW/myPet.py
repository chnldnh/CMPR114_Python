
import m9HW11_Proj1

def main():
    
    name = input('Pet name: ')
    type = input('Pet type: ')
    age = input('Pet age: ')
    # create pet object
    petName = m9HW11_Proj1.Pet(name, type, age)

     # retrieved the name from the external class
    print('The pet name is ', petName.get_name())

    # retrieved the pet type from the external class
    print('The pet type is ', petName.get_animal_type())

    # retrieved the age from the external class
    print('The pet age is ', petName.get_age())

# initialize main function
main()
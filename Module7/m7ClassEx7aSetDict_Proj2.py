
# m7ClassEx7a_project2

# this program uses a dicitonary to keep friends' 
# names and birthdays

# global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main funciton
def main():
    # create an empty dictionary
    birthdays = { }

    # inititalize a variable for the user's choice
    choice = 0

    while choice != QUIT:
        # get the user's menu choice
        choice = get_menu_choice()

        # process the choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

# the get_menu_choice funciton displays the menu
# and gets a validated choice fromn the user
def get_menu_choice():
    print()
    print('Friends and Thier Birthdays')
    print('----------------------------------------')
    print('1.  Look up a birthday')
    print('2.  Add a new birthday')
    print('3.  Change a birthday')
    print('4.  Delete a birthday')
    print('5.  Quit the prigram')
    print()

    # get the user's choice
    choice = int(input('enter your choice: '))

    # validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("enter a valid choice: "))

    # return the user's choice
    return choice

# the loop_up funciton looks up a name in the 
# birthdays dictionary
def look_up(birthdays):
    # get a name to look up
    name = input('Enter a name: ')

    # look it up in the dictionary
    print(birthdays.get(name, 'Not found. '))

# the add funciton adds a new entry into the 
# birthdays dictionary
def add(birthdays):
    # get a name and birthday
    name = input('Enter a name: ')
    bday = input('Enter a birthdays: ')

    # if the name does not exist, add it
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That entry already exists. ')

# the change function changes an existing
# entry in the birthdays dicitonary
def change(birthdays):
    # get a name to look up
    name = input("Enter a name: ")

    if name in birthdays:
        # get a new birthday.
        bday = input('Enter the new birthday: ')

        # Update the entry
        birthdays[name] = bday
    else:
        print('That name is not found.')    

# the delete function deletes and entry from the 
# birthdays dicitonary
def delete(birthdays):
    # get a name to look up
    name = input('Enter a name: ')

    # if the name is found, delete the entry
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')

# call the main function
if __name__ == '__main__':
    main()




                   
import m7Ex7aStrings_Ex2

class validate_m7ClassEx7aStrings_Ex2(object):
    """description of class"""

def main():
    #get a pw from the User
    password = input("enter your password: ")

    # validate the password
    while not m7Ex7aStrings_Ex2.valid_password(password):
        print('That password is not valid.')
        password = input("enter your password: ")

    print('That is a valid password.')

# call the main function
if __name__ == '__main__':
    main()
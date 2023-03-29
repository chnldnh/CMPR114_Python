 

import m7Ex7aStrings_Ex1
 
def main():
     first = input('enter your first name: ')
     last = input('enter your last name: ')
     idnumber = input('enter your idnumber: ')

     print('your system login name is: ')
     print(login.get_login_name(first, last, idnumber))

if __name__ == '__main__':
    main()


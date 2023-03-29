import m7Ex7aStrings_Ex1

class generate_m7Ex7aStrings_Ex1(object):
    """description of class"""

def main():
     first = input('enter your first name: ')
     last = input('enter your last name: ')
     idnumber = input('enter your idnumber: ')

     print('your system login name is: ')
     print(m7Ex7aStrings_Ex1.get_login_name(first, last, idnumber))

if __name__ == '__main__':
    main()


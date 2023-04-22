import m9Ch10ClassEx9_ChalEx4

def main():
    name = input('enter the name ')
    address = input('enter the address ')
    phone = input('enter the phone ')
    city = input('enter the city ')
    zipcode = input('enter the zipcode ')
    age = input('enter the age ')

    # calling class7 or the first file, then the name of the class, then the name of the function which equals to the input variables
    v1 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_name = name
    v2 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_address = address
    v3 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_phone = phone
    v4 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_city = city
    v5 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_zipcode = zipcode
    v6 = m9Ch10ClassEx9_ChalEx4.M9Ch10ClassEx9_ChalEx4.set_age = age

    print("Hello " + v1 + " your address is " + v2 + " and your # is " + v3 + '\n' + 'your city is ' + v4 +
          ' your zipcode is ' + v5 + ' and your age is ' + v6 )

main()



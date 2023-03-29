
# m7ClassEx7aStrings_Ex2

def get_login_name(first, last, idnumber):
    set1 = first[0 : 3]
    # get the first three letters of the last name
    # if the name is less than 3 characters, the
    # slice will return the entire last name
    set2 = last[0 : 3]

    # get the last three charaters of the student ID
    # if the ID number is less than 3 characters, the
    # slice will return the entire ID number
    set3 = idnumber[-3 :]

    #put the sets of characters together
    login_name = set1 + set2 + set3

    # return the login name
    return login_name

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(password) >= 7:
        correct_length = True

        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

        if correct_length and has_uppercase and \
            has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        return is_valid

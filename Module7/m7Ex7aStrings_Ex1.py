
# m7ClassEx7aStrings_Ex1


def get_login_name(first, last, idnumber):
    set1 = first[0 : 3] # get the first three letters of the first name

    set2 = last[0 : 3] # get the first three letters of the last name

    set3 = idnumber[-3 :] # get the last three letters of the idnumber

    login_name = set1 + set2 + set3 # put the sets together

    return login_name
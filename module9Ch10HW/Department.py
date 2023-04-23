import m9HW11_Proj2

class Department(object):
    """description of class"""

def main():
    acc = m9HW11_Proj2.Employee( 'Susan Meyers', 47899, 'Accounting', 'Vice President')
    IT = m9HW11_Proj2.Employee('Mark Jones', 39119, 'IT', 'Programmer')
    manu = m9HW11_Proj2.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer') 

    print(acc.getName(), acc.getidNum(), acc.getDept(), acc.getJobTitle())
    print(IT.getName(), IT.getidNum(), IT.getDept(), IT.getJobTitle())
    print(manu.getName(), manu.getidNum(), manu.getDept(), manu.getJobTitle())


# initiate function
main()




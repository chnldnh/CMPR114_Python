
#m6Ch6Ex5_1ChalEx4

def main():
    num_emps = int(input('enter the number of employee recoreds '))
    
    for count in range(1, num_emps +1):
        print('enter data for employee #', count)

        emp_file = open('C://employees.txt','w')
        name = input("Name: ")
        id_num = input("ID NUMBER: ")
        dept = input('DEPARTMENT: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

        emp_file.close()
        print('recorded')
main()

def Read():
    emp_file = open('C://employees.txt','r')
    fileContent = emp_file.read()
    emp_file.close()
    print(fileContent)
    
# Access the function
Read()
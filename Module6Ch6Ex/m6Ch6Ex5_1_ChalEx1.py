
#m6Ch6Ex5_1_ChalEx1

def write():
     fName = input("Enter first name ")
     lName = input("Enter last name ")
     age = input("Enter your age ")
     outFile = open('C://nameOutFile.txt', 'w') # write to a directory
   
     outFile.write(fName + ' ')
     outFile.write(lName + ', ')
     outFile.write(age)

     outFile.close()

     print('recorded successfully')

write()

def read():
    inFile = open('C://nameOutFile.txt', 'r')
    fileContents = inFile.read()
    inFile.close()
    print(fileContents)

read()






# m8MidTerm project 3
# Files and Exceptions

def write():
    try:
     coff = input("Enter your favorite coffee brand ")
     prod = input("Enter the prod number ")
     price = input("Enter the price ")
     outFile = open('C://Coffee.txt', 'w') # write to a directory
   
     outFile.write('Coffee' + '\t' + 'Prod Number' + '\t' + 'Price' + '\n')
     outFile.write(coff + '\t')
     outFile.write(prod + '\t\t')
     outFile.write('$' +price)

     outFile.close()

     print('recorded successfully')
    except Exception as err:
        print(err)
write()

def read():
    try:
        inFile = open('C://Coffee.txt', 'r')
        fileContents = inFile.read()
        inFile.close()
        print(fileContents)
    except Exception as err:
        print(err)

read()


# m8MidTerm project 4

def write():
    try:
     rent = float(input("Enter your rent "))
     gas = float(input("Enter your gas "))
     food = float(input("Enter your food "))
     clothing = float(input("Enter your clothing "))
     payment = float(input("Enter your car payment "))
     outFile = open('C://Expenses.txt', 'w') # write to a directory
   
     outFile.write(f'My expenses for the month.  Rent: ${rent:.2f}' + '\n')     
     outFile.write(f'My gas for the month.  gas: ${gas:.2f}' + '\n')    
     outFile.write(f'My food for the month.  food: ${food:.2f}' + '\n')    
     outFile.write(f'My clothing for the month.  clothing: ${clothing:.2f}' + '\n')    
     outFile.write(f'My payment for the month.  payment: ${payment:.2f}' + '\n')    

     outFile.close()

     print('recorded successfully')
    except Exception as err:
        print(err)
write()

def read():
    try:
        inFile = open('C://Expenses.txt', 'r')
        fileContents = inFile.read()
        inFile.close()
        print(fileContents)
    except Exception as err:
        print(err)

read()
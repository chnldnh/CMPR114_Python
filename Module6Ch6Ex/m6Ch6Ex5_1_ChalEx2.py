
#m6Ch6Ex5_1_ChalEx2

def WriteNumbers():
    outFile = open('C://numbers.txt', 'a') # open file to append
    num1 = int(input('enter #1 '))
    num2 = int(input('enter #2 '))
    num3 = int(input('enter #3 '))

    sum = num1 + num2 + num3 # sum input
    avg = sum/3 # average input

    outFile.write('the 1st number is ' + str(num1) + '\n')
    outFile.write('the 2nd number is ' + str(num2) + '\n')
    outFile.write('the 3rd number is ' + str(num3) + '\n')
    outFile.write('the avg number is ' + str(avg) + '\n')
    outFile.write('the total number is ' + str(sum) + '\n')

    print('data recorded')

WriteNumbers()

def ReadNumbers(): # read data
    innFile = open('C://numbers.txt', 'r')
    fileContent = innFile.read()
    innFile.close()
    print(fileContent)
    
# Access the function
ReadNumbers()


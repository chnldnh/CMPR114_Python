
#m5Ch5Ex4Part1ChalEx4

def add(num1, num2, num3):    
    global sum #declare global variable
    global average

    number1 = int(input('Enter 1st number: ')) # user input
    number2 = int(input('Enter 2nd number: '))
    number3 = int(input('Enter 3rd number: '))
    sum = num1 + num2 + num3 # get sum
    average = sum / 3 # get average
    return(sum, average)

add(3,4,5) # call add function, passing 3 parameters
print('sum ' + str(sum), 'average ' + str(average))


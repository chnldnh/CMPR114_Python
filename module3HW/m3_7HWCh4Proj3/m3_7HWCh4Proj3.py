
# m3 homework #3 Project #3
# Sum of Numbers

total = 0.0
num=0
num = int(input('enter a positive number (enter a negative number to end) '))

# continue as long as the user does not enter a negative number
while num > 0:
    total = total + num
    num = int(input('Enter a positive number (enter a negative number to end) '))    

# display the total of the numbers
print(f'total is {total}')

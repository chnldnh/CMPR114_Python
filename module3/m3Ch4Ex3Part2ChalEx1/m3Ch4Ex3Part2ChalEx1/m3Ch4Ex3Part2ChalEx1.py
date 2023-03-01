
# This program calculates the sum and average of a series
# of numbers entered by the user.

MAX = 5 # the maximum number

# Inititalize an accumulator variable
total = 0.0
ave = 0.0

# Explain what we are doing
print('This program calculates the sum of')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
    # Get the average
    ave = total/MAX

# Display the total of the numbers
print(f'The total is {total}.')
# Display the average of the numbers
print(f'The average is {ave}.')
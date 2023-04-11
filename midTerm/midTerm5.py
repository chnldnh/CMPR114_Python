
# m8MidTerm project 5

def main():
    numbers = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]   
    sum = 0  # create a variable for accumulator

    for value in numbers: # get the sum
        sum += value

    avg = sum/ len(numbers) # get the average

    print(f'The sum of the numbers is {sum}')
    print(f'The average of the numbers is {avg}')


# inititalize main function
main()

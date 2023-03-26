

# m6 homework #6_project4

def read():
    # Initialize an accumulator
    total = 0.0

    try:
        inFile = open('C://numbers.txt', 'r') # open to read the file

        # read the values from the file and accumulate them
        for line in inFile:
            amount = float(line)
            total += amount      

        inFile.close() # close the file
        print(f'{total:,.2f}') # print the total
    except Exception as err:
        print(err)

read()


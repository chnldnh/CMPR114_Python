# output numbers list to a text file
#m3_7Ch7ListChalEx4

def total():

    #create list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0

    for value in numbers:
        sum += value # total the numbers in the list

    average = sum /len(numbers) # the len functions returns the number of items in the list
    print('the total is ', sum, ' the average is ', average)

    for num in numbers: # pass the number to the list
        print(num)

    outfile = open ('C://num.txt', 'w') # open the file for writing

    outfile.write(str(numbers)) # write list into file

    outfile.close() # close the file

    print('recorded the names in the list ') # confirm recorded name

total()

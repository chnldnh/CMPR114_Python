# m3 homework #3 Project #2
# Average Rainfall

ALLMONTH = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
MONTH = 12

# Get the number of years.
numYear = int(input('What is the number of years?  '))

# Find the amount of rainfall for each month of each year.
for years in range(numYear):
    # Inititalize the accumulator
    total = 0.0
    print('Year', years + 1, ' of rainfalls')
    
    for month in ALLMONTH:
        inches = float(input(month + ' '))
        total += inches

totalInches = total

totalMonth = numYear * MONTH

ave = total / len(ALLMONTH)
 
print('The total number of months is: ', totalMonth) # total number of months
print('The total inches of rainfall is: ', totalInches) # total inches of rain
print('The average rainfall per month for the entire period is: ', ave) # Average
print()


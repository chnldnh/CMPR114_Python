# Bug Collector
# m3Ch4Ex3Part2ChalEx3

DAY = 5
totalBug = 0

#Get the number and accumulate
for bugs in range(DAY):

    bugs = int(input('Number of bugs collected for each day '))
    print(f' Bugs collected: {bugs} ')

    totalBug += bugs

#Display total number of bugs collected for 5 days
print(f' total number of bugs collected: {totalBug} ')
    
   
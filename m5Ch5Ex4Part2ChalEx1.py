
#m5Ch5Ex4Part2ChalEx1
# Kilometer Converter

KILORATE = 0.6214

def main():
    global kiloRate
    distKilo = float(input('Enter a distance in kilometer '))
    a=findDistance(distKilo) # call function with argument
    print('miles is ', a)

def findDistance(dKilo): # calculate miles function
    miles = dKilo * KILORATE
    return miles

# call main()
main()

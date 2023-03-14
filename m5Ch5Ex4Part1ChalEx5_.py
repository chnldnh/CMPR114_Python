
#m5Ch5Ex4Part1ChalEx5

def main():
    hrsWorked = float(input('Enter hours worked '))
    hourlyPay = float(input('Enter hourly pay '))
    # call function
    calWorkPay(hrsWorked, hourlyPay) # call function with 2 parameters
    return(hrsWorked, hourlyPay)

def calWorkPay(worked, pay): # create function
    print(f'hours worked {worked:,.2f} , hourly pay #{pay:,.2f}') # print hours worked and hourly pay

# call main function
main()

# m5Ch5Ex4Part2ChalEx2
# Automobile Costs

def main():   
    loanPayment = float(input('Enter a monthly costs for loan payment '))
    insurance = float(input('Enter a monthly costs for insurance '))
    gas = float(input('Enter a monthly costs for gas '))
    oil = float(input('Enter a monthly costs for oil '))
    tires = float(input('Enter a monthly costs for tires '))
    maintenance = float(input('Enter a monthly costs for maintenance '))
    mon, ann = monthlyCosts(loanPayment,insurance,gas,oil,tires,maintenance) # call function with argument
    print(f'total monthly expenses ${mon:,.2f}')
    print(f'total annual expenses ${ann:,.2f}')

def monthlyCosts(loan,ins,ga, oi, tir, maint): # calculate monthly expenses function
    month = loan + ins + ga + oi + tir + maint # calculate month expenses
    annual = month * 12 # cal annual expenses
    return month, annual

# call main()
main()





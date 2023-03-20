
# m5HW5Proj_3
# Monthly Sales Tax

STATETAX = .05
COUNTYTAX = 2.5

def main():
    monthSales = float(input('Enter total sales for the month '))
    a, b, c = calTax(monthSales)

    print(f'county sales tax ${a:,.2f}')
    print(f'state sales tax ${b:,.2f}')
    print(f'total sales + county tax ${c:,.2f}')
def calTax(mSales):
    resultCounty = mSales * COUNTYTAX # amount of county sales tax
    resultState = mSales * STATETAX # amount ofstate sales tax
    resultTotal =  resultCounty + resultState # total sales tax (county plus state)
    return resultCounty, resultState, resultTotal

#call function
main()

# m5HW5Proj_1
# Property Tax

PROPRATE = .60
PROPTAX = .72

def main():
    valueProp = float(input('What is the actual value of a piece of property '))
    aValue, pTax = calPropTax(valueProp) # call function with argument
    print(f'Assessment value is ${aValue:,.2f}') # print assessment value
    print(f'Property tax is ${pTax:,.2f}') # print property tax

def calPropTax(valProp): # function with 1 parameter
    assValue = valProp * PROPRATE; # find assessment value
    result = (assValue/100) * PROPTAX # find property tax
    return assValue, result

# call the main function
main()
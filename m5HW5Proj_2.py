
# m5HW5Proj_2
# Stadium Seating

CLASSA = 20
CLASSB = 15
CLASSC = 10

def main():
    ticktSoldA = int(input('How many tickets sold for Class A were sold?  '))
    ticktSoldB = int(input('How many tickets sold for Class B were sold?  '))
    ticktSoldC = int(input('How many tickets sold for Class C were sold?  '))
    resA = calTcktSoldA(ticktSoldA)  
    resB = calTcktSoldB(ticktSoldB)
    resC = calTcktSoldC(ticktSoldC)
    print(f'Class A ticket sale {resA:,.2f}')
    print(f'Class B ticket sale {resB:,.2f}') 
    print(f'Class C ticket sale {resC:,.2f}') 

def calTcktSoldA(soldA): 
    if soldA:
        resultA = soldA * CLASSA  
    return resultA

def calTcktSoldB(soldB): 
    if soldB:
        resultB = soldB * CLASSB   
    return resultB

def calTcktSoldC(soldC):
    if soldC:
        resultC = soldC * CLASSC  
    return resultC

# call function
main()
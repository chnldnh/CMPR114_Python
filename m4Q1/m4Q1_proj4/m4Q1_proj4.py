
#m4Q1_proj4

COMM5060 = .10
COMM7080 = .20
COMM90100 = .30

sales = float(input('Enter the sales '))

if sales > 50000.00 and sales < 70000.00:
    sales = (sales * COMM5060) + sales
    print(f'sales {sales:,.2f}' )      
elif sales >= 70000.00 and sales < 90000.00:
    sales = (sales * COMM7080) + sales
    print(f'sales {sales:,.2f}' )    
elif sales >= 90000.00 and sales < 100000.00:
    sales = (sales * COMM90100) + sales
    print(f'sales {sales:,.2f}' )   
else:
    print('reenter sales')
    

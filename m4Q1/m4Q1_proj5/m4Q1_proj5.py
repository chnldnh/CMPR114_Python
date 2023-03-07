
#m4Q1_proj5

COMM5060 = .10
COMM7080 = .20
COMM90100 = .30
SAL70 = 70000.00
SAL80 = 80000.00
SAL90 = 90000.00


sales = float(input('Enter the sales '))

if sales >= 50000.00 and sales < 70000.00:
    SAL70 = (SAL70 * COMM5060) + SAL70
    print(f'salary {SAL70:,.2f}' )      
elif sales >= 70000.00 and sales < 90000.00:
    SAL80 = (SAL80 * COMM7080) + SAL80
    print(f'salary {SAL80:,.2f}' )    
elif sales >= 90000.00 and sales < 100000.00:
    SAL90 = (SAL90 * COMM90100) + SAL90
    print(f'salary {SAL90:,.2f}' )    
    

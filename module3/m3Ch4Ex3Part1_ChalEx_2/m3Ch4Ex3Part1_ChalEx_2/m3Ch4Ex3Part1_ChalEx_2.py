
totSales = 0

for sales in [1, 2, 3, 4]:
    sales = float(input('Enter the sales '))
    commission = float(input('Enter the commission '))
    totSales = sales + commission
    print(f'sales + commission: ${totSales:,.2f}')
    

#m6Ch6Ex5_1_ChalEx3


def sales():
    totalSales = 0
    num_days = int(input('enter the days of sales ')) # days input from user
    salary = float(input('enter the salary ')) # salary input from user
    sales_file = open('C://sales.txt', 'a') # open files to append

    for count in range(1, num_days +1): # loop numbers of days, total sales
        sales = float(input('enter the sales for day # ' + str(count) + " : "))
        totalSales += sales   
        sales_file.write(f'sales: ${sales:,.2f}' + '\n') # write to file
   
    if totalSales > 1000: # cal total sales if over 1000
        salary = (salary * .10) + salary   # add 10% to salary
        sales_file.write(f'salary: ${salary:,.2f}' + '\n' + f'total Sales: ${totalSales:,.2f}') # write to file

    sales_file.close()
    print(f'sales and salaries recorded ' + ', ' + f'total sales: ${totalSales:,.2f} '+ ' ' + f'salary: ${salary:,.2f}')

sales()

def ReadSales(): # read file
    try:
        sales_file = open('C://sales.txt', 'r')
        line = sales_file.readline()
        while line != ' ':   
            amount = float(line)    
    except ValueError:
            amount = 0
            print(line)   
            line = sales_file.readline()   
    sales_file.close()

ReadSales()




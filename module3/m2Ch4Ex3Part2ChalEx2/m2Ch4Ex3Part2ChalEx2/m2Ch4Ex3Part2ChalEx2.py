#Challenge Ex #2

TIMER = 10 #const
another = 'y' # variable to control the loop

while another == 'y' or another == 'Y': # still loop while y
    num = int(input("Enter a number: "))  

    product = num * TIMER # calculation for product

    if product < 100: # continue looping 
        print(f'product: {product}')

    while product > 100: 
        print('product is greater than 100, try again') # product is > 100, so try again
        num = int(input('enter the correct number: '))   
        product = num * TIMER # recalculate product
        print(f'product: {product}')

    another = input('Do you have another item? (Enter y for yes): ')
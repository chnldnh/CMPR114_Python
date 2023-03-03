
# Total Sales App
#m3_7Ch7ListChalEx#4a

def main():
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sales = []

    for day in days:
        userInput = float(input('Enter the sales for ' + day + ": $" ))
        sales.append(userInput)
    total = sum(sales)
    print(f"Total sales: ${total:,.2f}")

    # open file to write
    outfile = open ('C://sales.txt', 'w')
    outfile.write(str(sales))

    outfile.close()

    print('recorded the names in the list ')

# Call th main function.
if __name__ == '__main__':
    main()






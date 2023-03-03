#Rainfall app
#m3_7Ch7ListExChalEx5
def main():
    rainMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #create empty list
    rain = []

    for rainfall in rainMonth:
        rainfall = float(input('Enter the total rainfall for each month ' + rainfall + ": "))
        rain.append(rainfall)
    total = sum(rain)
    print(f'Total rainfall is ', total) # get total rainfall

    average = total / len(rainMonth)
    print(f'Average rainfall is ', average) # get average rainfall

    print('The lowest rainfal is ', min(rain)) # get lowest rainfall
    print('The highest rainfal is ', max(rain)) # get highest rainfall

    # open file for writing
    outfile = open('C://rainfall.txt', 'w')
    outfile.write(str(rain)) # write list into the file

    outfile.close() # close the file

    print('recorded the names in the list ')

# Call th main function.
if __name__ == '__main__':
    main()

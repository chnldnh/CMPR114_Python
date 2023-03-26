
# m6 homework #6_project3

def write():   

        outfile = open('C://number_list.txt', 'w') # writing to the default directory
        try:

            for count in range(1, 101):
                number = int(count)
                outfile.write(f'{number}' + ' ')
              
            outfile.close() # close the file
            print('the numbers have been recorded')

        except Exception as err:
            print(err)

# call teh function
write()

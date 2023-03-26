
# m6 homework #6_project1

def write():   

        outfile = open('C://things.txt', 'w') # writing to the default directory
        try:
            outfile.write('elephant' + '\n')
            outfile.write('pinneapple' + '\n')
            outfile.write('Korea' + '\n')
   
            outfile.close()
            print('the names have been recorded')
        except Exception as err:
            print(err)
write()

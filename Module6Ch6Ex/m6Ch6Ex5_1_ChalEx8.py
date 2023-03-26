
#m6Ch6Ex5_1ChalEx8

import random

def main():
    try:
        # open a file for writitng
        outfile = open('C://Random.txt', 'w')

        for count in range(10):
             # get random number
             number = random.randint(1, 10)        
             outfile.write(str(number) + ' ')

        # close the file
        outfile.close()       
        
        print('successfully recorded!')
    
    except Exception as err:
        print(err)        

# call main function
main()

def Read():
    emp_file = open('C://Random.txt','r')
    fileContent = emp_file.read()
    emp_file.close()
    print(fileContent)
    
# Access the function
Read()

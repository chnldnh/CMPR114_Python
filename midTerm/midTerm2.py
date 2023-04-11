
# m8MidTerm project 2
# Files and Exceptions

def read():
    try:
        inFile = open('C://Coffee.txt', 'r') # open to read the file
        fileContents = inFile.read()
        inFile.close() # close the read file

        print(fileContents)
    except Exception as err:
        print(err)

read()


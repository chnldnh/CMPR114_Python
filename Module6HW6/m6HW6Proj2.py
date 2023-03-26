
# m6 homework #6_project2

def read():
    try:
        inFile = open('C://things.txt', 'r') # open to read the file
        fileContents = inFile.read()
        inFile.close() # close the read file

        print(fileContents)
    except Exception as err:
        print(err)

read()


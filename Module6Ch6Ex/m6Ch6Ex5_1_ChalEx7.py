
#m6Ch6Ex5_1ChalEx7

def main():
    try:
        # open a file for appending
        outfile = open('C://Grade.txt', 'a')

        # collect user input
        fullName = input('Enter a full name ')
        midtermGrade = int(input('Enter score of the midterm '))
        finalGrade = int(input('Enter score of the final exam '))

        avgGrade, letGrade = FindGrade(midtermGrade, finalGrade)
        outfile.write('Name: ' + fullName + '\n' + 'average grade is ' + str(avgGrade) + "\n" + 'letter grade is ' + str(letGrade))

        # Close the file
        outfile.close()
        print('The grade and names have been recorded')

    except Exception as err:
        print(err)        

def FindGrade(midTerm, final):
    
        total = midTerm + final
        avg = total / 2

        if avg > 100:
            print('Error: total grade too high')
        elif avg > 90 and avg < 100:
            letterGrade = 'A'
        elif avg > 80 and avg < 89:
            letterGrade = 'B'
        elif avg > 70 and avg < 79:
            letterGrade = 'C'
        elif avg > 60 and avg < 69:
            letterGrade = 'D'
        else:
            letterGrade = 'F'

        return avg, letterGrade

def ReadFile():
        # open the file
        infile = open('C://Grade.txt', 'r')
        # read the file's contents
        content = infile.read()
        # close the file
        infile.close()
        # print the data that was read into memory
        print(content)

# execute main function
main()

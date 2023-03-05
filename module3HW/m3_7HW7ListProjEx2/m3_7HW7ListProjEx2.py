# Number Analysis Program
#m3_7HW7ListProjEx2

NUM = 20

def main():
    seriesNum = [0] * NUM
    numList = []

    for index in range(len(seriesNum)):
        value = float(input(f'Enter a number {index + 1}: '))
        numList.append(value)
    total = sum(numList)
   
      # open a file for writing
    outfile = open('C:\\NumberAnalysisProgram.txt', 'w')

    # write the list to the file
    
    outfile.write(str(numList))

    # close the file
    outfile.close()

    print('File is successfully written.')

    print(f'Total ', total)  

    average = total / NUM
    print(f'average ', average)

    print(f'minimum ', min(numList))
    print(f'maximum ', max(numList))

    # call the main funciton
if __name__ == '__main__':
    main()


   
   


    


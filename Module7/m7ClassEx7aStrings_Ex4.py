
# m7ClassEx7aStrings_Ex4

# this program reads test scores from a CSV file
# and calculates each student's test average.

def main():
    csv_file = open('C://test_scores.csv', 'r') # open the file

    lines = csv_file.readlines() # read the file's lines into a list

    csv_file.close() # close the file

    for line in lines: # process the lines
        tokens = line.split(',') # get the test scores as tokens

        total = 0.0 # calculate the total ofthe test scores
        for token in tokens: 
            total += float(token)

        average = total / len(tokens) # calculate the average ofthe test scores
        print(f'Average: {average}')

if __name__ == '__main__': # execute the main function
    main()
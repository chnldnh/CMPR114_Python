
#m5Ch5Ex4Part1ChalEx1

# this program demonstrates two functions that 
# have local variables with the same name.

def main():
    texas()
    california()

def texas():
    birds = int(input('Enter numbers of birds - TX '))
    #birds = 5000
    print(f'texas has {birds} birds.')

def california():
    birds = int(input('Enter numbers of birds - CA '))
    #birds = 8000
    print(f'california has {birds} birds.')

main()

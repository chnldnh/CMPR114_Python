#Calories Burned
#m2Ch4Ex3Part2ChalEx4

CAL_BURN = 4.2
print('Minutes\tCalories_Burned') # heading
print('-------------------------------------')

for min in range(10, 35, 5):

    # Calculate calories burn per minute
    calBurn = min * CAL_BURN

    print(f'{min}\t{calBurn}') # display results


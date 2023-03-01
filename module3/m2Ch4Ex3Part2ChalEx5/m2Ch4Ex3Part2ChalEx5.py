# Lap Times
# m2Ch4Ex3Part2ChalEx5

fastest = 0
slowest = 0
average = 0
totalLaptime = 0
runLap = int(input('What is the number of times you run around the racetrack? '))

# get the starting value
#start = int(input('Enter the strting number: '))

# get the ending limite
#end=int(input('How high should I go '))
print('lap\ttime')
print('-----------------------')

# validate negative input
while runLap < 0: 
    runLap = int(input("Error: Enter a positive number "))

for lap in range(1, runLap + 1):

   lapTime = float(input('Enter lap times for each of the lap '))
  
   # validate negative input
   while lapTime < 0:
       lapTime = float(input('Error: enter a positive number'))

   if lap == 1:
           fastest = slowest = lapTime
   else:
           if lapTime > fastest:
               fastest = lapTime
           elif lapTime < slowest:
                slowest = lapTime

totalLaptime += lapTime

average = totalLaptime / runLap

print(f'{lap}\t{lapTime}')
print(f'Fastest lap {fastest}\n Slowest lap: {slowest} \n Average lap: {average}')
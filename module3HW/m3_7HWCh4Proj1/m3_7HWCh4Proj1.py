
# m3 homework #3 Project #1
# Distance Traveled

speed = int(input('What is the speed of the vehicle in mph?  ')) #Gets speed of the vehicle     
time = int(input('How many hours has it traveled?  ')) #Gets the hours
print('Hour \tDistance Traveled')
print('-----------------------------------')

for t in range(1, time +1):
    distance = speed * t 
    print(f'hours {t} ' + '\t', format(distance, '.0f'))



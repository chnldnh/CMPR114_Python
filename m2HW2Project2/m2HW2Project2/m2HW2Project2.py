

#m2Homework#2 Project#2
#Chanel Dinh 2/13/23
#Hot Dog Cookout Calculator

HOTDOGS_PER_PACKAGE=10
BUNS_PER_PACKAGE=8

totalPeople=int(input("What's the number of people attending the cookout "))
hotDogPerPerson=int(input("What's the number of hot dogs given per person? "))

#calculate number of hotdogs required
requiredHotDogs=totalPeople*hotDogPerPerson
packagesHotDogs=requiredHotDogs/HOTDOGS_PER_PACKAGE

#buns required
packagesBuns=requiredHotDogs/BUNS_PER_PACKAGE

print(f' Required hot dog package',  packagesHotDogs)
print(f' Required buns package', packagesBuns)

# remaining hotm dogs
remainHotDogs=requiredHotDogs % HOTDOGS_PER_PACKAGE
if remainHotDogs != 0:
    print(f' remaining hot dogs ', remainHotDogs)

remainBuns=requiredHotDogs % BUNS_PER_PACKAGE
if remainBuns != 0:
    print(f'  remaining buns ', remainBuns)









# m8MidTerm project 1
# calories from fat and carbohydrates

FATRATE = 9
CARBRATE = 4
def main():   
    fats = float(input(f"What is amount of carbohydrate grams you consumed in a day? "))    
    carbo = float(input(f"What is amount of fat grams you consumed in a day? "))    
    
    f, c = CalCalories(fats, carbo)

    print(f"calories from fats {f}, calorries from carbohydrate {c}")
def CalCalories(fat, carb):    
    reFat = fat * FATRATE
    reCarb = carb * CARBRATE
    
    return reFat, reCarb

  
#call function
main()
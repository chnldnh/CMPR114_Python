
# This program demonstrates the ProductionWorker class.

import manufacture

def main():       
        # Get the  the ProductionWorker's data.
        print("Enter the following ProductionWorker's data ")
        try:
            empName = input('Production Worker name? ')    
            empNum = input('Production Worker number? ')
            shiftNum = int(input('Production Worker shiftNum? 1 = Day, 2 or 3 = Night: '))    
            for shiftNum in [1,2,3]:
                if shiftNum == 1:  
                    shiftNum = 'Day'
                elif shiftNum == 2:
                    shiftNum = 'Night'
                elif shiftNum == 3:
                    shiftNum = 'Night'
            
            payRate = float(input('Production Worker payRate? '))
            #print('Make:', worker.get_make())
            #print('Model:', worker.get_model())
            #print('Mileage:', worker.get_mileage())
            #print('Price:', worker.get_price())
            #print('Number of doors:', used_car.get_doors())

            prodWorker = manufacture.ProductionWorker(empName, empNum, shiftNum, payRate)  # Create a ProductionWorker object

            # Display the data entered
            print()
            print('Data display')
            print('Production Worker name:', prodWorker.get_empName())
            print('Production Worker number:', prodWorker.get_empNum())
            print('Production Worker shiftNum:', prodWorker.get_shiftNum())
            print(f'Production Worker number:, ${prodWorker.get_payRate():,.2f}')
        except Exception as err:
                print(err)

# call the main function.
if __name__ == '__main__':
    main()
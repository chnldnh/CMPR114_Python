
#m13 Homewowrk #13, Project #1
# ShiftSupervisor is the subclass of Employee

import factory

def main():    
        try:
            shiftSup = factory.ShiftSupervisor('Emmy Smith', 'ER433', 1, 34.00, 50000, 600) # Create a ShiftSupervisor object

            # data for ShiftSupervisor
            print()
            print('Data display for shift supervisor')
            print('Shift Supervisor name:', shiftSup.get_empName())
            print('Shift Supervisor emp number:', shiftSup.get_empNum())
            print('Shift Supervisor shift:', shiftSup.get_shiftNum())
            print(f'Shift Supervisor pay rate: , ${shiftSup.get_payRate():,.2f}')
            print(f'Shift Supervisor annual salary: , ${shiftSup.get_annualSal():,.2f}')
            print(f'Shift Supervisor annual production bonus: , ${shiftSup.get_annualBon():,.2f}')

        except Exception as err:
                print(err)

# call the main function.
if __name__ == '__main__':
    main()

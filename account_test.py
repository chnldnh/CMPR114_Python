import m9Ch10ClassEx9_ChalEx5

def main():

        # Get the starting balance
        start_bal = float(input('Enter your starting balance: '))
        
        # Create a BankAccount object.
        savings = m9Ch10ClassEx9_ChalEx5.BankAccount(start_bal)

        #deposit the user's paycheck
        pay = float(input('How much were you paid this week? '))
        print('I will deposit that into your account. ')
        # the deposit function is passing one argument called amount
        # so we have to fulfill that argument with pay
        savings.deposit(pay)

        # retrieved the balanced from the external class
        print(f'yours account balance is ', format(savings.get_balance(), ',.2f'))
         
        cash = float(input('How muich would you like to withdraw? '))
        print('I will withdraw that from your account. ')
        # calls the withdraw function from the external class
        # and fulfills the one argument that is passed with cash
        savings.withdraw(cash)

        # retrieved the balanced from the external class
        print('your account balance is ', format(savings.get_balance(), ',.2f'))

    # call the main function
if __name__ == '__main__':
        main()


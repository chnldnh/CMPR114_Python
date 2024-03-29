
# m9Ch10ClassEx9_ChalEx5

class BankAccount:
    def __init__(self,bal): # the self is used to represent the instance of the class.
                                # it is used to access variables that belong to that class
        self.__balance = bal

    def deposit(self, amount):
    # add the balance"
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount:            
            self.__balance -= amount # subtract the balance
        else:
            print('error: insufficient funds')

    def get_balance(self):
        return self.__balance
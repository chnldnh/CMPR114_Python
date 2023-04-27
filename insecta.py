# m13 Ch11 Inheritance + class Ex #10
# Challenge Ex #5

class Insect:
    def __init__(self, type, eat):
        self.__type = type
        self.__eat = eat

    def get_type(self): # Create accessor method for __type attribute
        return self.__type

    def set_type(self, type): # Create mutator method for __type attribute
        self.__type = type

    def get_eat(self): # Create accessor method for __type attribute
        return self.__eat

    def set_eat(self, eat): # Create mutator method for __type attribute
        self.__eat = eat

# Bumblebee is the subclass of Insect
class Bumblebee(Insect):
    def __init__(self, type, eat, sting):  
        Insect.__init__(self, type, eat) # Call the superclass's __init__ method and pass arguments.

        # Inititalize the __sting attribute.
        self.__sting = sting

    def get_sting(self): # Create accessor method for __sting attribute
        return self.__sting

    def set_sting(self, sting): # Create mutator method for __sting attribute
        self.__sting = sting

# Grasshopper is the subclass of Insect
class Grasshopper(Insect):
    def __init__(self, type, eat, jump):
        Insect.__init__(self, type, eat) # Call the superclass's __init__ method and pass arguments.

        # Inititalize the __jump attribute.
        self.__jump = jump

    def get_jump(self): # Create accessor method for __jump attribute
        return self.__jump

    def set_jump(self, jump): # Create mutator method for __jump attribute
        self.__jump = jump
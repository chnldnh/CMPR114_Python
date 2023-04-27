# m13 Ch11 Inheritance + class ex #10
# chal ex #6

# The Automobile class holds general data
# about an automobile in inventory

class Automobile:

    # The __init__ method accepts arguments for the
    # make, model, mileage, and price.  It inititalizes 
    # the data attributes with these values.

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # The following methods are mutators for the 
    # class's data attributes.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The following methods are accessors for the 
    # class's data attributes.
        
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model 

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    # The Car class represents a car.  It is a subclass
    # of the Autotmobile class.

class Car(Automobile):
        # The __init__ method accepts arguments for the
        # car's make, model, mileage, price, and doors.

    def __init__(self, make, model, mileage, price, doors):
       # Call the superclass's __init__ method and pass
       # the required arguments.  Note that we also have
       # to pass self as an argument.
       Automobile.__init__(self, make, model, mileage, price)
            
       #  Inititalize the __door attribute.
       self.__doors = doors
           
    # The set_doors method is the mutator for the 
    # __doors attribute.

    def set_doors(self, doors):
        self.__doors = doors

    # The get_ddors method is the accessor for the 
    # __doors attribute.

    def get_doors(self):
        return self.__doors

# The Truck class represents a pickup truck.  It is aa
# subclass of the Automobile class.

class Truckl(Automobile):
    # The __initi__ mothod accepts arguments for the 
    # Truck's make, model, mileage, price, and drive type.

    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclas's __init__method and pass
        # the required arguments.   Note that we also have
        # to passself as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the __drive_type attribute.
        self.__drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # __drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    # The get_drive_type method is the accessor for the
    # __drive_type attribute.

    def get_drive_type(self):
        return self.__drive_type

# The SUV class represents a sport utility vehicle.  It
# is a subclass of the Autobobile class.

class SUV(Automobile):
    # The __init__ method accepts arguments for the 
    # SUV's make, model, mileage, price, and passenger
    # capacity.

    def __init__(self, make, model, mileage, price, pass_cap):
        # CAll the superclas's __init__ method and pass
        # the required arguments.  Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap
    # the set_pass_cap method is the mutator for thew 
    # __pass_cap attribute

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the 
    # __pass_cap attribute.

    def get_pass_cap(self):
        return self.__pass_cap

# The Electric class represents a Electric vehicle.  It is a subclass
# of the Autotmobile class.

class Electric(Automobile):
        # The __init__ method accepts arguments for the
        # car's make, model, mileage, price, and engine.

    def __init__(self, make, model, mileage, price, engine):
       # Call the superclass's __init__ method and pass
       # the required arguments.  Note that we also have
       # to pass self as an argument.
       Automobile.__init__(self, make, model, mileage, price)
            
       #  Inititalize the __engine attribute.
       self.__engine = engine
           
    # The set_engine method is the mutator for the 
    # __engine attribute.

    def set_engine(self, engine):
        self.__engine = engine

    # The get_engine method is the accessor for the 
    # __doors attribute.

    def get_engine(self):
        return self.__engine



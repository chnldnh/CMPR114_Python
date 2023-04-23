
# m9HW11_Proj3
# RetailItem Class

class RetailItem:
    def __init__(self, desc, inventory, price):
        self.__desc = desc
        self.__inventory = inventory
        self.__price = price

    def getDesc(self):
        return self.__desc

    def getInventory(self):
        return self.__inventory

    def getPrice(self):
        return self.__price

    def setDesc(self, desc):
        self.__desc = desc

    def setInventory(self, inventory):
        self.__inventory = inventory

    def setPrice(self, price):
        self.__price = price

import m9HW11_Proj3

class inventory(object):
    """description of class"""

def main():
    # create objects
    item1 = m9HW11_Proj3.RetailItem('Jacket', 12, 59.95)
    item2 = m9HW11_Proj3.RetailItem('Designer Jeans', 40, 37.95)
    item3 = m9HW11_Proj3.RetailItem('Shirt', 20, 24.95)

    print('Item # 1')
    print(item1.getDesc())
    print(item1.getInventory())
    print(item1.getPrice())
    print()

    print('Item # 2')
    print(item2.getDesc())
    print(item2.getInventory())
    print(item2.getPrice())
    print()

    print('Item # 3')
    print(item3.getDesc())
    print(item3.getInventory())
    print(item3.getPrice())
    print()
   
# initiate function
main()
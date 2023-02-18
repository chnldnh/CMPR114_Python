
#Chanel Dinh 2/13/23
#m2Homework#2 Project#3
#Software Sales

RETAIL=99

countQuantity=int(input('Enter the number of packages purchased '))

if countQuantity>=10 and countQuantity<=19:
    print(f' Subtotal ${(countQuantity * RETAIL):.2f}')
    print(f' Discount 10% ${((countQuantity * RETAIL) * .10):.2f}')
    print(f' Total ${(countQuantity * RETAIL) - ((countQuantity * RETAIL) * .10):.2f}')    
elif countQuantity>=20 and countQuantity<=49:
    print(f' Subtotal ${countQuantity * RETAIL:.2f}')
    print(f' Discount 20% ${((countQuantity * RETAIL) * .20):.2f}')
    print(f' Total ${(countQuantity * RETAIL) - ((countQuantity * RETAIL) * .20):.2f}')
elif countQuantity>=50 and countQuantity<=99:
    print(f' Subtotal ${(countQuantity * RETAIL):.2f}')
    print(f' Discount 30% ${((countQuantity * RETAIL) * .30):.2f}')
    print(f' Total ${(countQuantity * RETAIL) - ((countQuantity * RETAIL) * .30):.2f}')
elif countQuantity>=100:
    print(f' Subtotal ${(countQuantity * RETAIL):.2f}')
    print(f' Discount 40% ${(countQuantity * RETAIL) * .40:.2f}')
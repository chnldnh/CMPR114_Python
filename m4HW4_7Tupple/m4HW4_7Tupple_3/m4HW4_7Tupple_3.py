
#m4HW4_7Tupple_3

# initializing tuple
test_tup = ([17, 28], [93, 11], [20, 17])
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Using map() + list() + sum() to sum
tupSum = sum(list(map(sum, list(test_tup))))
 
# printing result
print("The sum of tuple: " + str(tupSum))
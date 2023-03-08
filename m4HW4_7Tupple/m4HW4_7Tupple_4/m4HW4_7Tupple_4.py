
#m4HW4_7Tupple_4

# list initialisation
input_tup = [(2, 20), (44, 1), (3, 13)]   

print('original list', input_tup)
  
# Passing lambda as key to sort list of tuple
print('sorted list', sorted(input_tup, key = lambda x: x[0] + x[1]))

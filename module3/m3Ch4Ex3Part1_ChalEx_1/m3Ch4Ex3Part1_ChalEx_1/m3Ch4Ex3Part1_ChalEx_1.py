
TEMPP = 102.5
avg = 0
totTemp = 0
count = 0

temp = float(input("Enter the temp "))

while temp < TEMPP:
 
  totTemp += temp #temp to add to total temp
  count += 1 #counter
  avg = totTemp/count #calculate average

  print(f'total: {totTemp}, ' + f'average: {avg}') 
  temp = float(input("Enter a temp "))

#m4Q1_proj1

ADDSAL = .10

salary = float(input('Enter the gross salary '))
salary = (salary * ADDSAL) + salary

print(f' Total salary ${(salary):,.2f}')
import os
os.system('clear')

print('--- Start ---\n')
print('Variables')

number = 12
string = ' -string-  '
fracrion = 45.33
print("Int: %d, Str: %s, Fraction number: %d" %(number, string, fracrion))

str_number = str(number)
str_fraction = str(fracrion)
print('Convert to string: ' + str_number + string + str_fraction)

x = 10
y = 7
print(x + y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)
print(x % y)


print('\n--- End ---', end='\n'*4)

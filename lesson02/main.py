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
print('\nx=%d, y=%d' %(x, y))
print('Додавання x+y: ', x + y)
print('Віднімання x-y: ', x - y)
print('Множення x*y: ', x * y)
print('Ділення: x/y', x / y)
print('Підняття до степеня x^y: ', x ** y)
print('Цілочисельне ділення x//y: ', x // y)
print('Остача від цілочисельного ділення x%y: ', x % y)


print('\n--- End ---', end='\n'*4)

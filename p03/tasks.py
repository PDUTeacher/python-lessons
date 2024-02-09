# Check if a given number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# Determine if a person is eligible to vote based on their age.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Determine the largest of three numbers.
a = int(input("Enter three numbers separated by space: "))
b = int(input("Enter three numbers separated by space: "))
c = int(input("Enter three numbers separated by space: "))
if a >= b and a >= c:
    print(f"{a} is the largest.")
elif b >= a and b >= c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")


# ----
number = int(input("Please enter a number: "))
if number > 10:
     print("Python conditions and loops are a piece of cake.")
else:
     for i in range(number):
         print("I am back to check on my skills!")

# ----
a = 7
if a >= 2 and a <= 8:
    print('OK')


# ----
age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")

# ----
x = int(input("Прошу ввести ціле число: "))
if x < 0:
    x = 0
    print('Негативне число замінено на нуль: x=', x)
elif x == 0:
    print('Нуль')
elif x == 1:
   print('Один')
else:
    print('Більше 1')
# ------ 1
# Write a Python program to display the first and last colors from the following list.
import random

color_list = ["Red","Green","White" ,"Black"]
print("%s %s" % (color_list[0], color_list[-1]))

# ------ 2
# Print the elements of a list.
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)


# ------ 3
# Generate the random 100 elements of a list.
my_list = []
for i in range(100):
    print(my_list.append(random.randint(0, 100)))

print(my_list)

# ------ 4
# Write a Python program to count the input number in a given list.
nums = [1, 4, 6, 7, 4, 4, 7, 1, 2, 8]
count = 0
n = input()

for num in nums:
    if num == n:
        count = count + 1

print(count)


# ------ 5
# Write a Python program to create a histogram from a given list of integers.
histogram = [12, 31, 6, 54, 9]
for i in histogram:
    print('')
    for h in range(i):
        print("#", end='')

print('')


# Reverse a list.
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)


# ------ 6
# Remove Duplicates from a List
numbers = [1, 2, 3, 2, 4, 1, 5, 6, 3]
unique_lst = []

for num in numbers:
    if num not in unique_lst:
        unique_lst.append(num)

print("Unique numbers:", unique_lst)





# ---- Write file
#numbers = [x for x in range(1, 20, 2)]
#numbers.insert(0,40)

# file = open('numbers.txt', 'w')
# for n in numbers:
#     file.write("%s\n" % n)
# file.close()


# ---- Read file
# numbers = []
# ---- 1
# file = open('numbers.txt', 'r')
# for x in file.readlines():
#     numbers.append(int(x))
# ---- 2
# with open('numbers.txt', 'r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         numbers.append(int(line))

# --- 1
#for i in range(5):
#    print('Number: ', i)

# --- 2
#for i in range(4):
#    print('Number: ', i)
#else:
#    print('End of cycle!')

# --- 3
#step = 6
#for i in range(100, 120, step):
#    print('Number: ', i, ' step: ', step)

#for i in range(-100, 20, 10):
#    print('Number: ', i)


# --- 4
# import random
#
# # random.randint(a, b)
# #x = random.randint(0, 100)
# #print(x)
# #x = random.randint(-200, 0)
# #print(x)
# # random.randrange(start, stop[, step])
# #x = random.randrange(0, 100, 5)
# #print(x)

# --- 5
# s = 'Text'
# for i in s:
#     print(i)

# --- 6
# Знайти всі прості числа з діапазону
#a = 0
#b = 100
#for n in range(a, b + 1):
#    is_prime = True
#    for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#            is_prime = False
#    if is_prime:
#        print('%d, ' % n,  end='')


# Таблиця множення
#for j in range(10):
#    print('\n')
#    for i in range(10):
#        print(f'{j}*{i}=\033[94m{j*i}\033[0m', end=' ')


# # --- 7
# # https://en.wikipedia.org/wiki/List_of_Unicode_characters
# import random
# attempts = 4
# rating = 0
# print("\u2591" * 40, )
# print("\u2591" * 4, ' Guess the number from 0 to 4 ', "\u2591" * 4)
# print("\u2591" * 8, f'  You have {attempts} attempts ', "\u2591" * 8)
# print("\u2591" * 40, end='\n'*2)
#
# for i in range(1, attempts+1):
#     print('Step \u21D2 [', i, ']  ', end='')
#     random_number = random.randint(1, 4)
#     number = int(input(' Input number: '))
#     if random_number == number:
#         rating += 1
#         print(' \033[92m \u261D You guessed it!, You rating: %d \033[0m' % rating)
#     else:
#         print('  \033[91m \u26D4 Number = %d, you answer = %d.' % (random_number, number), end="")
#         if i < attempts:
#             print('  Try again, you have %d attempts \033[0m' % (attempts-1))
#         else:
#             print('\n \033[0m')
#
# print("\u2593" * 40, )
# print("\u2593" * 12, f'You rating: {rating} ', "\u2593" * 12)
# print("\u2593" * 40, )


# ---
#import random
#points_number = 0
#print("Гра складається з 5-ти раундів.")
#print("В кожному раунді я загадую випадкове исло від 1 до 5. Твоя задача його вгадати.")
#print("Якщо відповідь правильна, ти отримуєш 2 бали.")
#print("Якщо твоє число відрізняється від мого на 1, ти отримуєш 1 бал.")
#for Round in range(1, 6):
#    print("Раунд %s" % Round)
#    print("Ваша відповідь:")
#    user_choise = int(input())
#    number = random.randint(1,5)
#    print("Загадане число: %s" %number)
#    if user_choise == number:
#        points_number += 2
#        print("Ви отримали 2 бали")
#    elif user_choise - number == 1:
#        points_number += 1
#        print("Ви отримали 1 бал")
#    elif user_choise - number == -1:
#        points_number += 1
#        print("Ви отримали 1 бал")
#    print()
#print("Вітаємо, ваш результат за всю гру: %s" % points_number)









# --- a.1
#days = ['Monday', 'Tuesday', 'Wednesday']
#fruits = ['banana', 'orange', 'apple']
#drinks = ['coffee', 'tea', 'beer']
#for day, fruit, drink in zip(days, fruits, drinks):
#    print(day, ": drink", drink, "eat", fruit)
#numbers = [1, 2, 3]
#for number in numbers:
#    print('Цей список має деякі елементи', number)
#    break
#else:
    # Відсутність переривання означає, що елемент відсутній
#    print('Елементів немає в списку, чи не так?')


#  prints table of formatted text format options
# for style in range(8):
#     for fg in range(30,38):
#         s1 = ''
#         for bg in range(40,48):
#             format = ';'.join([str(style), str(fg), str(bg)])
#             s1 += '\x1b[%sm [%sm \x1b[0m' % (format, format)
#         print(s1)
#     print('\n')


# bcolors_HEADER = '\033[95m'
# bcolors_OKBLUE = '\033[94m'
# bcolors_OKCYAN = '\033[96m'
# bcolors_OKGREEN = '\033[92m'
# bcolors_WARNING = '\033[93m'
# bcolors_FAIL = '\033[91m'
# bcolors_ENDC = '\033[0m'
# bcolors_BOLD = '\033[1m'
# bcolors_UNDERLINE = '\033[4m'
# print(f"{bcolors_WARNING}Warning: No active frommets remain. Continue?{bcolors_ENDC}")
# print(f"{bcolors_HEADER}Header: No active frommets remain. Continue?{bcolors_ENDC}")

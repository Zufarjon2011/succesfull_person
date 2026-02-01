#Урок №5 задание 3
import random

name = input('ведите ваше имя:')
print('Добро пожаловать', name , "в игру 'Угадай число' ")

min_num = 1
max_num = 5

secret_num = random.randint(min_num, max_num)
while True:
    guess = int(input("Угадайте число от {} до {}: ".format(min_num, max_num)))
    if guess > secret_num:
        print("Загаданное число больше")
    elif guess < secret_num:
        print("Загаданное число меньше")
    else:
        print("Поздравляю", name ,"Вы угадали число!")
        break
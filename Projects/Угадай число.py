from time import sleep
from random import randrange
import random
sleep(1)
name = input('enter your name: ')
print(name + " Welcome to game 'Угадай число' ")

min_num = 1
max_num = 5

secret_num = random.randint(min_num, max_num)
while True:
    guess = int(input("find number {} to {}: ".format(min_num, max_num)))
    if guess > secret_num:
        print("secret number is small but your is big")
    elif guess < secret_num:
        print("secret number is big but your is small")
    else:
        print("Congratulations", name ,"you have find a number and now you are on second lvl!")
        break
sleep(randrange(1,5))

min_num = 1
max_num = 10

secret_num = random.randint(min_num, max_num)
while True:
    guess = int(input("find number {} to {}: ".format(min_num, max_num)))
    if guess > secret_num:
        print("secret number is small but your is big")
    elif guess < secret_num:
        print("secret number is big but your is small")
    else:
        print("Congratulations", name ,"you have find a number and now you are on Third lvl!")
        break
sleep(randrange(1,5))
    
min_num = 15
max_num = 20

secret_num = random.randint(min_num, max_num)
while True:
    guess = int(input("find number {} to {}: ".format(min_num, max_num)))
    if guess > secret_num:
        print("secret number is small but your is big")
    elif guess < secret_num:
        print("secret number is big but your is small")
    else:
        print("Congratulations", name ,"you have find a number and now you are on second lvl!")
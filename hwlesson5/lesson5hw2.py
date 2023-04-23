#Урок №5 задание 2
while True:
    age = int(input('Введите свой возраст: '))
    if age == 0:
        print('вы только что родились :)')
    elif age < 19 or age == 18 :
        print('вам еще есть чтобы водить автомобиль!')
    elif age < 25 or age == 45:
        print('вы будете мастер по водить автомобиль')
    elif 18 < age < 65:
        print('вы уже можете водить автомобиль!')
    elif age > 71:
        print('будьте осторожным когда водите автомобиль!')
    countine = input('Продолжыть игру? [Y/N] ')
    if countine == str('n'):
        print('выход!')
        break
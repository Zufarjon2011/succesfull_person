##Урок №4 задание 7
agenow = int(input('ведите ваш возраст: '))

if agenow:
    if agenow <= 19:
        print('Вам нужно учиться')
    elif agenow < 50:
        print('Вам нужно работать')
    elif agenow <= 59:
        print('Вам скоро на пенсию')
    elif agenow <= 111:
        print('вы пенсионер')
    else:
        print('вы поставили рекорд!')
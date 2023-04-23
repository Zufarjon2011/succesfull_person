##Урок №4 задание 9
number1 = int(input('ведите первый число: '))
number2 = int(input('ведите вторую число: '))
number3 = int(input('ведите третий число: '))

if number1 == number2 and number2 == number3:
    print('Кол-во совпадающих:3')
elif number1 == number2 or number2 == number3 or number1 == number3:
    print('Кол-во совпадающих:2')
else:
    print('Кол-во совпадающих:0')

##Урок №4 задание 2
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

nums = number1 + number2

if nums % 5 == 0:
   nums += 1
else:
   nums -= 2

print("Результат:", nums)
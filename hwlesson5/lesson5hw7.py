#Урок №5 задание 7
symma = float(input("Введите сумму вклада: "))
year = int(input("ведите количество лет: "))

nums = 0.1
vse = symma

for i in range(year):
    vse += vse * nums

print("Сумма на счету через", year, "лет:", round(vse, 2))
#Урок №5 задание 5
count = 0

for i in range(100000, 1000000):
    digits = [int(d) for d in str(i)]
    if sum(digits[:3]) == sum(digits[3:]):
        print(i)
        count += 1

print("Количество счастливых билетов:", count)

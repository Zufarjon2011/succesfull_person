#Урок №5 задание 6
height = int(input("Введите высоту ёлки: "))
symbol = input('ведите симбол!:')

for i in range(1, height+1):
    print(" "*(height-i) + symbol *(2*i-1))

print(" "*(height-1) + "*")
##Урок №4 задание 13
width = int(input('ведите width: '))
length = int(input('ведите length: '))
parts = int(input('ведите parts: '))

parrt = (width * length)

if parrt % parts == 0:
    print('YES')
elif parrt % parts != 0:
    print('NO')
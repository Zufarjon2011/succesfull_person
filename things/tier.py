#import datetime
#from time import sleep
#
#data = int(input("Укажите время для таймера (в минутах): "))
#timer = str(datetime.timedelta(minutes=data))  # Конвертация минут в ЧАС:МИНУТА:СЕКУНДА
#h, m, s = timer.split(":")  # Распаковка элементов списка
#h, m, s = int(h), int(m) - 1, int(s)  # всегда должно быть на минуту меньше

#for hour in range(h, -1, -1):
#    for minute in range(m, -1, -1):
#        for second in range(59, -1, -1):  print(f'\{rhour}):{minute}:{second}', end=' ', flush=True)



num1 = input('ведите высоту ёлки:')

print(num1.replace('5', '*'))
print('''*
      ***
      *****
      ******
      ''')

#BAAAAAAAAAAAAD calc v1
#creator @zufar_BRO ZUFRAJON XOJIAKBAROV :)
operation = input('enter operation[*,/,+,-,%,//,**]: ')
a = float(input('enter first num: '))
b = float(input('enter second num: '))
eq1 = a * b
eq2 = a / b
eq3 = a + b
eq4 = a - b
eq5 = a % b
eq6 = a // b
eq7 = a ** b
if operation == '*':
    print('it is equal to ', eq1)
    eq1 = a * b
elif operation == '/':
    print('it is equal to ', eq2)
    eq2 = a / b
elif operation == '+':
    print('it is equal to ', eq3)
    eq3 = a + b
elif operation == '-':
    print('it is equal to ', eq4)
    eq4 = a - b
elif operation == '%':
    print('it is equal to ', eq5)
    eq5 = a % b
elif operation == '//':
    print('it is equal to ', eq6)
    eq6 = a // b
elif operation == '**':
    print('it is equal to ', eq7)
    eq7 = a ** b
else:
    print("sorry i can't understand what are you meaning")

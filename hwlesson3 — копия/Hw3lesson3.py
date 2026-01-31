##Урок 3 задание 3
str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '

str1 = str1.lower()
print(str1.replace('<<', '  ')[1:10:1])
str2 = str2.lower()
print(str2[:10:1])
str3 = str3.lower()
print(str3.replace('((', '  ')[1:10:])
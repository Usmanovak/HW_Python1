'''Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

Пример:
385916 -> yes
123456 -> no
'''

num = int(input('Number of ticket: '))

if num > 0:
    if num // 10**5 + num // 10**4 % 10 + num // 10**3 % 10 == num % 10**3 // 100 + num % 100 // 10 + num % 10:
        print ('Lucky ticket')
    else: print('Simple ticket')
else: print ('error')
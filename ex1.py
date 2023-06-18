'''
Задача 2: Найдите сумму цифр трехзначного числа.

Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

n = int(input('Enter a three-digit number: '))
sum = 0
x = 0

while n > 0:
    x = n % 10
    sum += x
    n //= 10
else: print(sum)
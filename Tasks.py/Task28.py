# Задача 28: Напишите рекурсивную функцию sum(a, b), 
#возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2

def sum(a, b):
    if b == 0:#если одно из чисел равно нулю, то возвращается второе число
        return a
    elif b > 0:#если оба числа больше 0
        return sum(a + 1, b - 1)#функция вызывает себя с увеличенным первым и уменьшиным вторым
    else:
        return sum(a - 1, b + 1)#если меньше 0, то наоборот

a = int(input('Введите значение А: '))
b = int(input('Введите значение B: '))

result = sum(a, b)
print(result)

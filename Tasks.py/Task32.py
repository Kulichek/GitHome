#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


a1 = int(input("Введите первый элемент прогрессии: ")) #задача 30. определяем первый элемент прогрессии,разность и количество элементов
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progress = [] #создаем прогрессию для хранения значений
for i in range(n):
    progress.append(a1 + i*d)

min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

index = []#создаем список для хранения индексов элементов в диапазоне
for i in range(len(progress)):#перебираем все элементы прогрессии
    if min <= progress[i] <= max:#если элемент в диапазоне
        index.append(i)# добавляем в список 

print("Список элементов прогрессии:", progress)
print("Индексы элементов, принадлежащих заданному диапазону:", index)
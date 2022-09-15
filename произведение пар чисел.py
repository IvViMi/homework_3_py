# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
os.system('cls||clear')
print('Определение произведения пар чисел равноудалённых')
print('Задайте массив из 5 чисел')
your_list = []
for i in range(5): 
    num = int(input('Введите целое число: '))
    your_list.append(num)
print(f'Заданный массив: {your_list}')

multipli_list = []
for i in range((len(your_list)+1)//2):
    multipli_list.append(your_list[i]*your_list[len(your_list)-1-i])
print(multipli_list)

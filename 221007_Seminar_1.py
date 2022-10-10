"""
задача 1. Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:*
- 6 -> да
- 7 -> да
- 1 -> нет

Решение 1 задания:
"""
print("Решение 1 задания:")

week_day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
day_off = ['Рабочим днем', 'Выходным днем']
day_input = int(input("Введите день недели: "))
day = None

try:
    for i in range(len(week_day)):
        if day_input-1 == i:
           day = week_day[i]
    if 0 < day_input < 6:
        print(f"Вы ввели {day_input}, что соответствует такому дню недели как {day}, и является {day_off[0]}.")
    else:
        print(f"Вы ввели {day_input}, что соответствует такому дню недели как {day}, и является {day_off[1]}.")
except:
    print(f"Вы ввели {day_input}, что не соответствует какому-либо дню недели и является некоректными данными.")

"""

задача 2. Напишите программу для
проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.

Решение 2 задания:
"""

print("Решение 2 задания:")
x = input("Введите значение Х: ")
y = input("Введите значение У: ")
z = input("Введите значение Z: ")

if not (x or y or z) == (not x and not y and not z):
    print("Истина")
else:
    print("Ложь")


"""

задача 3. Напишите программу, которая принимает на вход
координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
*Пример:*
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

Решение 3 задания:
______________________
"""

print("Решение 3 задания:")
x = int(input("Введите координату Х: "))
y = int(input("Введите координату Y: "))
plane = [
            [f"Введены координаты {x,y}.", "Точка находится в четверти №:", "Точка находится на оси:", "Точка находится в начале коородинат. "],
            ["I", "II", "III", "IV", "V", "X", "Y"]
        ]
if (x > 0 and y > 0):
    print(plane[0][0], plane[0][1], plane[1][0])
elif (x < 0 and y > 0):
    print(plane[0][0], plane[0][1], plane[1][1])
elif (x < 0 and y < 0):
    print(plane[0][0], plane[0][1], plane[1][2])
elif (x > 0 and y < 0):
    print(plane[0][0], plane[0][1], plane[1][3])
elif (x == 0 and y != 0):
    print(plane[0][0], plane[0][2], plane[1][5])
elif (x != 0 and y == 0):
    print(plane[0][0], plane[0][2], plane[1][6])
elif (x == 0 and y == 0):
    print(plane[0][0], plane[0][3], "Хотя по условиям задачи, такие данные не должны были быть введены.")
    
"""
задача 4 HARD необязательная Напишите простой калькулятор, 
который считывает с пользовательского ввода три строки: 
первое число, второе число и операцию, после чего применяет 
операцию к введённым числам ("первое число" "операция" "второе число") и
выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.
Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!
Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0
Sample Input 3:
5.0
10.0
/
Sample Output 3:
0.5

Решение 4 задания:
______________________
"""
print("Решение 4 задания:")
num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
num_3 = 1
operation = str(input("Введите операцию, какую бы хотели произвести над числами, из предложенных (+, -, /, *, mod, pow, div): "))
operation_list = ["+", "-", "/", "*", "mod", "pow", "div"]
answer_list = ["Результат равен: "]
for i in range(len(operation_list)):
    if operation == operation_list[i]:
        print(f"Будет вычислена следующая операция: \n{num_1} \n{num_2} \n{operation}")

if operation == operation_list[0]:
    print(f"{answer_list[0]} {num_1 + num_2}")
elif operation == operation_list[1]:
    print(f"{answer_list[0]}  {num_1 - num_2}")
elif operation == operation_list[2]:
    if num_2 == 0:
        print(f"Второе введенное Вами число = {num_2}, на {num_2} делить нельзя!")
    else:
        print(f"{answer_list[0]}  {num_1 / num_2}")
elif operation == operation_list[3]:
    print(f"{answer_list[0]}  {num_1 * num_2}")
elif operation == operation_list[4]:
    if num_2 == 0:
        print(f"Второе введенное Вами число = {num_2}, на {num_2} делить нельзя!")
    else:
        print(f"{answer_list[0]}  {num_1 % num_2}")
elif operation == operation_list[5]:
    num_3 = num_1 ** num_2
    print(f"{answer_list[0]}  {num_3}")
elif operation == operation_list[6]:
    if num_2 == 0:
        print(f"Второе введенное Вами число = {num_2}, на {num_2} делить нельзя!")
    else:
        print(f"{answer_list[0]}  {num_1 // num_2}")

"""
Задача 5 VERY HARD SORT необязательная
Задайте двумерный массив из целых чисел. 
Количество строк и столбцов задается с клавиатуры. 
Отсортировать элементы по возрастанию слева направо и сверху вниз.
Например, задан массив:
1 4 7 2
5 9 10 3
После сортировки
1 2 3 4
5 7 9 10

Решение 5 задания:
______________________
"""

print("Решение 5 задания:")
import random

row = int(input("Введите количество строк думерного массива: "))
col = int(input("Введите количество столбцов думерного массива: "))
array_list = []

for i in range(row):
    array_list.append([0] * col)

for k in range(len(array_list)):
    for y in range(col):
        array_list[k][y] = random.randrange(0, 100)
print()
print(f"Сгенерирован двумерный массив, состоящий из {row} строк и {col} столбцов:\n {array_list}")
print()

print("Так удобнее:")
for a in array_list:
    for b in a:
        print(b, end = ' ')
    print()

array_list_sorted = []

for q in array_list:
    for s in q:
        array_list_sorted.append(s)
array_list_sorted.sort()
array_list = array_list_sorted

array_list = [array_list[i:i+col] for i in range(0, len(array_list), col)]
print()

print("Ответ на задание:")
for a in array_list:
    for b in a:
        print(b, end = ' ')
    print()

'''
1. Сумма трех
Посчитайте сумму трех введенных целых чисел

2. Площадь
Пользователь вводит стороны прямоугольника, выведите его площадь

3. Одинаковая четность
Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".

4. Одно положительное
Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".

5. Меньшее из двух
Пользователь вводит два целых числа. Выведите меньшее из них.

6.Четырехзначное?
Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
'''
# ========================================
# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# c = int(input("Ведите третье число: "))
# print("Сумма трех чисел", a+b+c)
# ========================================
# a = int(input("Ведите сторону a: "))
# b = int(input("Ведите сторону b: "))
# print("Площадь прямоугольника ", a*b)
# ========================================
# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# if a%2==b%2:
#     print(" а и b имеют одинаковую четность")
# else:
#     print(" а и b имеют разную четность")
# ========================================
# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# c = int(input("Ведите третье число: "))
#
# if a >= 0 or b >= 0 or c >= 0:
#     print("Хотя бы одно число положительно")
# else:
#     print("Ни одно число не положительно")
# ========================================
#
# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
#
# print(a if a < b else b)
# ========================================
# a = int(input("Ведите  число: "))
# print("yes" if a >= 1000 and a <= 9999 else "No")
# ========================================

# РЕШЕНИЯ В ГРУППАХ

# ========================================
# Задача No1. Решение в группах
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2
# 
# a = int(input("Ведите длинну маршута: "))
# b = int(input("Ведите сколько проезжает машина в день : "))
# print("Машина проедит весь путь за ", (a+b-1)//b) // -(-a//b)
# ========================================
# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
#
# a = int(input("Ведите  число учеников в 1 классе: "))
# b = int(input("Ведите число учеников в 2 классе: "))
# c = int(input("Ведите число учеников в 3 классе: "))
# print(-(-a//2 + -b//2 + -c//2))
# ========================================
# Задача No5. Решение в группах
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6
# a = int(input("Введите  порядковый от головы куда он сел : "))
# b = int(input("Введите номер на табличке: "))
#
# if a!=b:
#     print("В поезде количество вагонов", a-1+b )
# else:
#     print("Не достаточно данных")
# ========================================
# Задача No7. Решение в группах
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016 Output: YES
# 15 минут
# a = int(input("Ведите  год для проверки на високосность: "))
# if a%400==0 or (a%4==0 and a%100!=0):
#     print("yes")
# else:
#     print("no")
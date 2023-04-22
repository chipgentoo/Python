'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''
# ========================= РЕШЕНИЕ =========================
# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))

# def power(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * power(a, b - 1))

# print(f'{b}-я cтепень числа {a} равна:', power(a, b))
# ===========================================================
'''
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения:
Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза, к нему добавляется количество повторений.
'''
# ========================= РЕШЕНИЕ =========================

# import random

# def gen_str():
#     mch = 32 # макс. кол-во одной буквы
#     mchs = random.randint(0,25) # кол-во используемых букв
#     out_str = ''
    
#     for i in range(mchs): # цикл по буквам
#         char_num = random.randint(ord('A'), ord('Z'))
#         for j in range(0,random.randint(0,mch)): # цикл по кол-ву
#             out_str += chr(char_num)
#     return out_str

# def rle(in_string):
#     out_string = ""
#     i = 0
#     while (i <= len(in_string)-1):
#         count = 1
#         ch = in_string[i]
#         j = i
#         while (j < len(in_string)-1): 
#             if (in_string[j] == in_string[j + 1]): 
#                 count = count + 1
#                 j = j + 1
#             else: 
#                 break
#         out_string = out_string + ch + str(count)
#         i = j + 1
#     return out_string

# in_str = gen_str()
# print('Исходная строка:')
# print(in_str)

# encode_str = rle(in_str)
# print(encode_str)

# ===========================================================
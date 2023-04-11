'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
'''
# ========================= РЕШЕНИЕ =========================
import random
n = int(input("Введите кол-во монет: "))
eagle = 0
tails = 0
coin = []
for i in range(n):
    coin.append(random.randrange(0,2))
    if coin[i] != 0:
        eagle += 1
    else:
        tails += 1
print(coin)
if eagle > tails:
    print("Переворачиваем орлов")
else:
    print("Переворачиваем решки")

# ===========================================================
'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
# ========================= РЕШЕНИЕ =========================
S = int(input("Введите сумму чисел"))
P = int(input("Введите произведение чисел"))

# ===========================================================
'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
'''
# ========================= РЕШЕНИЕ =========================
# ===========================================================

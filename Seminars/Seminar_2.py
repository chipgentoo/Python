# Вводятся числа, пока не введут 0. Найти сумму четных чисел

# a = [1, 2, 3, 4, -5]
# ind = 0
# while x := input() != 0:
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)

# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)

# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])

# a = []
# a.append(10)
# print(a)

# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)

# =============================================================
# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
#
# n = int (input ("Введите число "))
# i = 1
# fact = 1
#
# while i <= n:
#     fact *= i
#     i += 1
# print (fact)

# =============================================================
# 11. Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
#
# A = int (input("Введите число "))
# i = 0
# k = 1
# j = 0
# count = 1
# while j < A:
#     j = i + k
#     k = i
#     i = j
#     count += 1
# if A == j:
#     print(count)
# else: print(-1)

# =============================================================
# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
#
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# N = int (input("Введите количество дней "))
# count = 0
# count_max = 0
# for _ in range (N):
#     temp = int(input("Введите температуру "))
#     if temp > 0:
#          count += 1
#          if count_max < count:
#              count_max = count
#     else: count = 0
# print (count_max)


# =============================================================
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

"""
    Problem 1

    Multiples of 3 or 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Вариант 1 - полный перебор с проверкой.

sum = 0  # Обнуляем сумму

for i in range(1, 1000):  # Перебираем диапазон от 1 до 999
    if i % 3 == 0 or not i % 5:  # Проверяем остаток от деления: на 3 сравнение с нулём, на 5 через отрицание нуля
        sum += i  # Суммируем

print(sum)

# Вариант 2 - суммируем с заданным шагом.

sum = 0

for i in range(3,1000,3):
    sum += i

for i in range(5,1000,5):
    if i % 3:
        sum +=i

print(sum)

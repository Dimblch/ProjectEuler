"""
    Problem 12

    Highly divisible triangular number

    https://projecteuler.net/problem=12
"""
import time


def count_divisors(num):
    list = []  # Список с делителями
    i = 1  # Первый делитель на проверку
    while i <= num // i:
        if num % i == 0:
            list.append(i)
            if i == num // i:
                break
            list.append(num // i)
        i += 1
#    list.sort()
#    print(num, ": ", len(list), ":", list)
    return (len(list))


num = 0  # Первое треугольное число
i = 0  # Счётчик итераций цикла
divisors = 1

start_time = time.time()

while divisors <= 500:
    i += 1
    num += i
    divisors = count_divisors(num)

print("Треугольное число : ", num)
print("Количество слагаемых треугольного числа :", i)

stop_time = time.time()

print("Выполнение заняло:", stop_time - start_time, "сек.")

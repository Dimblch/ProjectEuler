"""
    Problem 12

    Highly divisible triangular number

    https://projecteuler.net/problem=12
"""
import time


def count_divisors(num):
    list = [1]  # Список с делителями
    i = 2  # 1 уже в списке, начинаем проверку с 2
    while i < num / 2 + 1:
        if num % i == 0:
            if i > num // i:
                break
            list.append(i)
            list.append(num // i)
        #            count += 1
        i += 1
    list.append(num)
    list.sort()
    print(num, ": ", len(list), ":", list)
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

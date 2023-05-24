"""
    Problem 10

    Summation of primes

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""
sum = 0
list_of_primes = [i for i in range(1, 2000000)]
list_of_primes[0] = 0       # Зануляем единицу в списке простых чисел

for i in list_of_primes:        # Проходимся по списку
    if i != 0:
        j = 2 * i
        while j < len(list_of_primes)+1:        # И зануляем все значения кратные ещё не зануленным
            list_of_primes[j-1] = 0  # Не забываем что нумерация списка начинается с 0
            j += i

for p in list_of_primes:        # Суммируем всё что осталось
    sum += p

print(sum)

"""
    Problem 7

    10001st prime

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
"""

# TBD Очень затратный по ЦПУ алгоритм, надо будет переписать, когда-нибудь.

list_of_prime = [2,3]       # Стартовое заполнение списка простых чисел
applicant = list_of_prime[-1] + 1       # Претендент на звание следующего простого числа

while len(list_of_prime) < 10001:
    applicant += 1
    flag = 1
    for prime in list_of_prime:
        if applicant % prime == 0:
            flag = 0
            break
    if flag:
        list_of_prime.append(applicant)
        applicant += 1      # Сразу накидываем единичку, поскольку два простых подряд быть не может.

print(list_of_prime[10000])  # Выводим 10001ое простое число (не забываем что нумерация элементов начинается с нуля)

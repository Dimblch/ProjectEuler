"""
    Problem 5

    Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Искомое число есть произведение простых делителей чисел от 1 до 20

divisors = [1,2,2,2,2,3,3,5,7,11,13,17,19]
product = 1

for i in divisors:
    product *=i

print(product)

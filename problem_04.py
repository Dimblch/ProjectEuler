"""
    Problem 4

    Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 12321     # Первый пришедший на ум палиндром от произведения 111*111

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j     # Перемножаем все трёхзначные числа друг с другом
        reversed_product = int(str(product)[::-1])      # Переворачиваем результат через преобразование в строку
        if reversed_product == product and product > largest:
            largest = product

print(largest)

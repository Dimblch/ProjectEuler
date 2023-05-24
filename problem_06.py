"""
    Problem 6

    Sum square difference

    https://projecteuler.net/problem=6
"""

sum_of_squares = 0
sum = 0
square_of_sum = 0

for i in range(1,101):
    sum_of_squares += i*i
    sum += i

square_of_sum = sum * sum

print(square_of_sum - sum_of_squares)

"""
    Problem 14

    Longest Collatz sequence

    https://projecteuler.net/problem=14
"""

def collatz(number):
    counter = 1
    while number != 1:
        counter +=1
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    return (counter)

longest = 0
number = 1

for i in range(1,1000000):
    length = collatz(i)
    if length > longest:
        longest = length
        number = i

print("Число:", number)
print("Длинна последовательности:", longest)

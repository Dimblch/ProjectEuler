"""
    Problem 9

    Special Pythagorean triplet

    https://projecteuler.net/problem=9
"""

for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a+b+c == 1000:
                if a*a + b*b == c*c:
                    print(a,' ',b,' ',c)
                    print(a * b * c)
                    exit()

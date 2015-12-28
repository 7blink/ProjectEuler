"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
def compute():
    max = 1000

    #create a loop within a loop within a loop to run every combination of a,b,c
    for b in range(1,max):
        for a in range(1,b):
            c = max - a - b
            if (a**2) + (b**2) == (c**2):
                return a*b*c

if __name__ == "__main__":
    print(compute())

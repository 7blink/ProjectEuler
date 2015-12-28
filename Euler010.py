"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def compute():
    max = 2000000
    runningTotal = 2
    for i in range(3, max, 2):
        if isPrime(i):
            runningTotal += i

    return runningTotal

#isPrime is described in Euler #7
def isPrime(testNumber):
    divisor = 3
    while True:

        if divisor**2 > testNumber:
            return True

        if testNumber % divisor == 0:
            return False

        else:
            divisor += 2


if __name__ == "__main__":
    print(compute())

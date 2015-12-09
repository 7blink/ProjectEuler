#!/usr/bin/python3
"""
Problem 7
Published on Friday, 28th December 2001, 06:00 pm; Solved by 248583; Difficulty rating: 5%

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math
def compute():
    currentNumber = 3
    count = 1
    #Test each number
    #If prime, add count +1
    #If count is 10001, print result
    while True:
        if isPrime(currentNumber):
            count += 1
        if count == 10001:
            return currentNumber
        else:
            currentNumber += 2

#Test to see if number is prime
def isPrime(testNumber):
    #divisors only need to be prime numbers greater than 2.
    divisor = 3
    while True:
        #only need to check up to sqrt of number
        if divisor > math.sqrt(testNumber):
            return True
        if testNumber % divisor == 0:
            return False
        else:
            divisor += 2

if __name__ == "__main__":
	print(compute())

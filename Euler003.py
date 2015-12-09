"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def compute():
    import math
    number = 600851475143
    divisor = 2
    largestPossible = math.sqrt(number)
    while True:
        if divisor > largestPossible:
            return number
        else:
    #if number is divisable by divisor, store number and divide
    #then check again if same number is a factor again
            if number % divisor == 0 :
                number = number / divisor
    #only need to check up to the sqrt of the number
                largestPossible = math.sqrt(number)
            else:
                divisor = divisor + 1


if __name__ == "__main__":
	print(compute())

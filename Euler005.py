"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#To make the program efficient, only check lowest common multiple
#LCM of prime numbers is the primes multiplied together
#So 2*3*7*11*13*17*19 = 9699690
#So only check muliples of 9699690

def compute():
    tempNumber = 9699690
    while True:
        if multiple(tempNumber) == True:
            return tempNumber
        else:
            tempNumber = tempNumber + 9699690

#Only need to check 11-20 because they are multiples of 1-10
def multiple(tempNumber):
    for x in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
        if tempNumber % x != 0:
            return False
            break
    return True

if __name__ == "__main__":
	print(compute())

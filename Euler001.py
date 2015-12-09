"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def compute():
    max = 1000
    currentNumber = 3
    total = 0

    #Check every number below max
    while currentNumber < max:
    #If number is divisable, add to total
        if ((currentNumber % 3 == 0) or (currentNumber % 5 == 0)):
            total += currentNumber
        currentNumber += 1

    return total



if __name__ == "__main__":
	print(compute())

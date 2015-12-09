"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def compute():
    tempHighest = 0
    #Create a for loop within a for loop to have every combination
    #Start with the largest to save processes
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            x = a * b
    #Only if the product is higher do we check if it is a palindrome
            if tempHighest < x:
                if str(x) == str(x)[::-1]:
                    tempHighest = x
                else:
                    continue
    return tempHighest



if __name__ == "__main__":
	print(compute())

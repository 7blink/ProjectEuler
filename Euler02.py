"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def compute():

    #There are 4 variables
    #The first number to add
    #The second number to add
    #Then the current fibonacci number
    fibonacci = 3
    runningTotal = 2
    fibFirst = 1
    fibSecond = 2

    while fibonacci < 4000000:
        #If current fibonacci meets requirements, add to runningTotal
        if fibonacci % 2 == 0:
            runningTotal = runningTotal + fibonacci

        #To calc new fibonacci number, shift the current numbers over and then add the two highest to get a new fibonacci
        fibFirst = fibSecond
        fibSecond = fibonacci
        fibonacci = fibFirst + fibSecond

    return runningTotal

if __name__ == "__main__":
    print(compute())

"""
Find a 10 digit number where each digit identifies the number of times that digit appears.  So the first digit is how many zeros are in the number, the second digit is how many ones are in the number, ect ect until the last digit is how many nines are in the number.
"""
import time
start = time.time()
def compute():
    min = 1000000000
    max = 10000000000
    #Starting with a 1 in the "zeros" count because if it was lower then it would be zero, which would make the zero's count 1.
    for i in range(7000000000, 10000000000):
        number = i
        number_string = str(number)
        count = 0
        success = True
        for place in range(0,10):
            count = 0
            for digit in number_string:
                if str(place) == digit:
                    count += 1
            if number_string[place] == str(count):
                continue
            else:
                success = False
        if success == True:
            print("Number Found")
            print(number)

if __name__ == "__main__":
    compute()
    elapsed = time.time() - start
    print ("%d seconds" % (elapsed))

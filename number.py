#1/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1-100."""
print("Guess the number!")

#x = random.randint(1,100)
x = random.binomialvariate(1,0.7)
guess=None
print(x)
while x !=guess:

    guess=int(input("Pick a number between 1 to 100:"))

    if x==guess:
        print ("You genius!")
    #elif x>guess:
    #    print ("Try a bingger number.")
    #elif x<guess:
    else:
        print("haha")
main()


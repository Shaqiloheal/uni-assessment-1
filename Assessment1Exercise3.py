# Author: Warren Spalding - SID: 52199280
# Date: 25/10/2021
# CS1032 Assessment 1: Exercise 3
# Program that uses a recursive function to calculate the result of a positive number
# 'n' raised tp the power of another positive number 'p'.

def recurse(n, p):

    if p == 0:
        return 1

    elif p == 1:
        return n

    else:
        return (n * recurse(n, p - 1))
        
n = int(input("Please input base number as an integer: "))
p = int(input("Please input exponent as an integer: "))

print(n, "to the power of", p, "is" , recurse(n, p))

    



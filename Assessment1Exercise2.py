# Author: Warren Spalding - SID: 52199280
# Date: 25/10/2021
# CS1032 Assessment 1: Exercise 2
# Program that asks the user to input their weight and height which calls a function
# that recieves the weight and height and calculates the BMI.  The BMI result is then
# displayed and rounded to 1 decimal place.  Another function is then called from the
# recieved BMI value and prints out a message describing the catergory the BMI falls under.

import math

def bmi(weight, height):
    return (weight / math.pow(height, 2)) #math library used to square height in formula

def catergoryBmi(returnBmi):
    if returnBmi < 18.5:
        print("The BMI is in the underweight catergory.")

    elif returnBmi < 25:
        print("The BMI is in the healthy catergory.")

    elif returnBmi < 30:
        print("The BMI is in the overweight catergory.")

    elif returnBmi < 40:
        print("The BMI is in the obease catergory.")

    else:
        print("The BMI is in the severely obease catergory.")
        
    

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters to 2 decimal points: "))
returnBmi = bmi(weight, height)

print("You current BMI is: ", round(returnBmi, 1)) #Print value is rounded to 1 decimal place

catergoryBmi(returnBmi) #calls function catergoryBmi

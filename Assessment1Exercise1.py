# Author: Warren Spalding - SID: 52199280
# Date: 25/10/2021
# CS1032 Assessment 1: Exercise 1
# Program that calculates the area of a trapezium.

def trapArea(valueA, valueB, valueHeight): #Function containing trapesium formula
    return ((valueA + valueB) / 2) * valueHeight
    
valueA = float(input("Please enter length of side A of Trapesium: "))
valueB = float(input("Please enter length of side B of Trapesium: "))
valueHeight = float(input("Please enter height of Trapesium: "))

print("The area of the Trapesium is: ", trapArea(valueA, valueB, valueHeight)) #Prints area of trapesium given by users chosen variables


    





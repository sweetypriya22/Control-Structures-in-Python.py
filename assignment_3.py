'''Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*(factorial(n-1))
factorial_5 = factorial(5) 
print("Factorical of 5 is",factorial_5)

'''Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

'''

from math import sqrt, log, sin, radians 
def calculate_math(num):
    square_num = sqrt(num)
    log_num = log(num)
    sine_num = sin(radians(num))
    return square_num, log_num, sine_num
num = float(input("Entre a number:"))

calculated_results = calculate_math(num)
print(calculated_results)
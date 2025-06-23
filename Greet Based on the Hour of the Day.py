#Greet Based on the Hour of the Day
'''
Write a program that takes an integer input representing the hour of the day (in 24-hour format) and returns an appropriate greeting message: 

"Good morning!" for hours from 5 (inclusive) to 12 (exclusive)
"Good afternoon!" for hours from 12 (inclusive) to 17 (exclusive)
"Good evening!" for hours from 17 (inclusive) to 5 (exclusive)

Constraints:
The input hour will be an integer in the range 0 to 23 (inclusive).
Minutes or seconds will not be considered; only the hour matters.

Input Format:
A single integer denoting the hour of the day in 24-hour format.
Note: Decimal or floating-point numbers are not valid inputs. 
'''
 # Taking input
hour = int(input())

def greet(h):
    if 5 <=  h < 12:
        return "Good morning!"
    elif 12<= h < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Print the output 
print(greet(hour))








#Armstrong number
'''
Write a function that checks whether a number is an Armstrong number. 
A number is Armstrong if the sum of the cubes of its digits is equal to the number itself.

Input Format:
An integer num

Output Format:
Yes if the number is Armstrong, else No
'''
#Taking input
num = int(input())

def is_armstrong(num):
    # Write your code 
    total = 0
    New = num 
    while New > 0:
        digit = New % 10
        total += digit**3
        New //=10


    return "Yes" if total == num else "No"

# Print the output
print(is_armstrong(num))
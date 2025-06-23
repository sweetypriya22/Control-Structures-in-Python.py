#Reverse a Number Without Converting to String
'''
Write a program to reverse a Non-Negative Integer without converting it to a String.

The program should take an Integer and return the Integer Reversed.
Input Format:

Non-Negative Integer.
Output Format:

The Reversed Integer.

Constraints:
The input is a Non-Negative Intege.
'''
# Taking input
num = int(input())
count = 0
def reverse_number(n):
    # Write your code
    global count
    while n>0:
        digit = n % 10
        count = count * 10 + digit
        n = n//10
    return count
        #reversed_num = reversed_num * 10 + digit
        #n = n // 10  
# Print the output
print(reverse_number(num))

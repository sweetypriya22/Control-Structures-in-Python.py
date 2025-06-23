#recursive function
'''
Write a recursive function to calculate the sum of the digits of a given number.
Input Format:
 An integer n
Output Format:
An integer representing the sum of the digits of n
'''
 # Taking input
n = int(input())

def sum_of_digits(n):
    # Write your code 
    if n==0:
        return 0
    else:
        New = n%10
        return New+sum_of_digits(n//10)
# Print the output
print(sum_of_digits(n))
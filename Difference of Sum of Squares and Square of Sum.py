#Difference of Sum of Squares and Square of Sum
'''
Write a program that calculates the difference between the sum of the squares and the square of the sum for the first n natural numbers.
Specifically, given a positive integer n, compute:

The sum of the squares: 1² + 2² + ... + n²
The square of the sum: (1 + 2 + ... + n)²
Return the difference: (square of the sum) - (sum of the squares).

Input Format:
A single integer n representing the number of natural numbers.

Output Format:
An integer representing the difference between the square of the sum and the sum of the squares of the first n natural numbers.
'''


# Taking input
n = int(input())

def difference_sum_squares(n):
# Write your code here
    sum_squares = 0
    for i in range(1,n+1):
        total_sum_of_n = n*(n+1)//2
        squares_sum = total_sum_of_n**2
        sum_squares = sum(i*i for i in range(1, n+1))
        

        diff = (squares_sum - sum_squares)
        return diff
# Print the output
print(difference_sum_squares(n))
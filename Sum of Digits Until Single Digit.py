#Sum of Digits Until Single Digit
'''
Write a Python function 'sum_until_single_digit(num)' that takes a Non-Negative Integer number 
and repeatedly sums its digits until the result is a single digit. 
Return that single-digit sum.

For example, given number = 9875, 
The sum of digits is 9+8+7+5 = 29,
then sum digits of 29 → 2+9 = 11, and
Finally, sum the digits of 11 → 1+1 = 2.
The function returns 2.

Input Format:

A single non-negative integer num.

Output Format:

Return the single-digit integer obtained by repeatedly summing the digits of the number.

Constraints:
0 <= n<= 109
'''
num = int(input())

def sum_until_single_digit(num):
    # Write your code 
    while num>=10:
        count = 0
        for i in str(num):
            count+=int(i)
            num = count
    return num
# Print the output
print(sum_until_single_digit(num))
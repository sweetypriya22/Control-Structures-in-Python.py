#Check for Perfect Number
'''
Check for Perfect Number
Write a function 'check_perfect_number(n)' that checks whether a given number n is a perfect number. 
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).
Input Format:
A single integer n 
Output Format:
Return True if the number is perfect, otherwise return False.
Constraints:
n is a positive integer (1≤n≤106)
'''
import math
n = int(input("Entre number:"))
perfect_num = n
def check_perfect_number(n):
    global perfect_num
    if n<=0:
        return False
    total = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n
print(check_perfect_number(n))

#Check if a Number is a Strong Number

'''
Write a program to check whether a given number is a Strong Number or not.
A Strong Number is a number whose sum of the factorial of each digit is equal to the number itself.

For example,
145 is a strong number because: 1! + 4! + 5! = 1 + 24 + 120 = 145.

Input Format:
A single integer number.

Output Format:
Print True if the number is a Strong Number; otherwise, print False.
'''
# Taking input
n=int(input())

def factorial(n):
   # Write Your Code here
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

def is_strong_number(number):
   # Write Your Code here
   if number == 0:
        return False
   original = number
   num = 0
   while number > 0:
      digit = number % 10
      num+=factorial(digit)
      number//=10

   return num==original 
# Print the output 
print("True" if is_strong_number(n) else "False")














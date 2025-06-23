#Pyramid Pattern Using Arithmetic Operations
'''
Write a program to print a Pyramid Pattern of numbers, where each row contains the row number repeated.
Input Format:
5
Single integer n — number of rows.
Output Format: 
The output should be in Pyramid Pattern with each row containing the row number repeated, each on a new line.
'''
# Taking input
n = int(input())

def print_pyramid(n):
    # Write your code
     for i in range(1,n+1):
        print (str(i)*i)
# Print the output
print_pyramid(n)
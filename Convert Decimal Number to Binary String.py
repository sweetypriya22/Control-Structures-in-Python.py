#Convert Decimal Number to Binary String
'''
Write a Python function 'decimal_to_binary(num)' that converts a Non-Negative Decimal Integer number 
to its Binary representation as a String. 



Input Format:

A single non-negative integer number.



Output Format:

Return a string representing the Binary equivalent of the input decimal number.
'''

num = int(input())
def decimal_to_binary(num):
    # Write your code here
    if num == 0:
        return "0"
    
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2
    
    return binary_str
# Print the output
print(decimal_to_binary(num))
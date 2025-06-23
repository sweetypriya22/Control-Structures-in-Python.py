#Print Zigzag Number Pattern
'''
Write a Python function print_zigzag(n) that prints numbers from 1 to n in a zigzag pattern across three rows.
The zigzag pattern follows this repeating cycle every 4 numbers:

1st number in row 1
2nd number in row 2
3rd number in row 3
4th number in row 2

Each number is followed by a space. 
Positions without a number should be filled with two spaces "  " to maintain alignment.

Input Format:
A single integer n representing the total number to print in the zigzag pattern.

Output Format:
Print 3 lines, each containing the numbers arranged in the zigzag pattern separated by spaces, with appropriate spacing for alignment.
'''
# Taking input  
num = int(input())

def print_zigzag(n):
    row1 = ""
    row2 = ""
    row3 = ""
    # Write your code here
    for i in range(1, n+1):
        zig = i % 4
        if zig==1:
            row1+= str(i)
            row2+= " "
            row3+= " "
        elif zig==2:
            row1+= " "
            row2+= str(i)
            row3+= " "
        elif zig==3:
            row1+= " "
            row2+= " "
            row3+= str(i) 
        elif zig==0:
            row1+= " "
            row2+= str(i) 
            row3+= " "
        
        
    print(row1)
    print(row2)
    print(row3)      
         
# Print the output
print_zigzag(num)







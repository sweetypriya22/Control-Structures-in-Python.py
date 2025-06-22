# Control Structures in Python.py
Control Structures in Python
'''Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''
num = int(input("Enter num:"))
if num %2==0:
    print(num , "is an even number.")
else:
    print(num, "is an odd number.")
     

'''Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''
count = 0
for i in range(1,51):
    count+=i
print(count)

#Print Identity Matrix
'''
Print Identity Matrix
Write a program that prints an N x N Identity Matrix Pattern.
An Identity Matrix is a square matrix where all the elements on the main diagonal (from the top-left to the bottom-right corner) are 1, and all other elements are 0.

Input Format:
A single integer N  
Output Format:
Print the N x N identity matrix pattern, with numbers in each row separated by spaces, and each row on a new line.
Constraints:

N is an integer.
1 <= N <= 15
'''

#taking input
N = int(input("Entre number:"))
# Print Identity Matrix
def print_identity_matrix(N):
    # Write your code here
    for i in range(N):
        row = ""
        for j in range(N):
            if i == j:
                row += "1"
            else:
                row += "0"
        print(row)
# Print the output
print_identity_matrix(N)
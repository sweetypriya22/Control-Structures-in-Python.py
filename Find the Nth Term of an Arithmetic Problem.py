#Find the Nth Term of an Arithmetic Problem
'''
Find the Nth Term of an Arithmetic Problem
Write a function 'find_nth_arithmetic_term(a, d, n_term)' that finds the 'n_term-th' value in the arithmetic progression.
In an arithmetic progression (AP), each term after the first is obtained by adding a constant value called the common difference, d, to the previous term.
The first term is denoted by a, and the 'n_term-th' term can be computed using the formula:
T(n)=a+(n_term−1)×d
Where:
a: the first term of the progression.
d: the common difference between consecutive terms.
'n_term': the position of the term you want to find (e.g., 1st, 2nd, 3rd term).

Input Format:
Three inputs, each on a separate line:
a: Integer (no restrictions specified on magnitude).
d: Integer (no restrictions specified on magnitude).
n_term: Integer, where 1 ≤ n_term ≤ 100
Output Format:
An integer representing the 'n_term-th' value in the arithmetic progression.
Constraints:
The first term a (integer).
The common difference d (integer).
The term number 'n_term' (positive integer, 1 ≤ n_term ≤ 100).
'''

#taking input
a = int(input("First term:"))
d = int(input("Common_diff:"))
n = int(input("n_term_th:"))
def find_nth_arithmetic_term(a, d, n):
    # Code to find the nth term in an arithmetic progression
    return a + (n - 1) * d
print(find_nth_arithmetic_term(a, d, n))


#or 
def find_nth_arithmetic_term():
    a = int(input("First term:"))
    d = int(input("Common_diff:"))
    n_term = int(input("n_term_th:"))
    return a + (n_term - 1) * d
print(find_nth_arithmetic_term())



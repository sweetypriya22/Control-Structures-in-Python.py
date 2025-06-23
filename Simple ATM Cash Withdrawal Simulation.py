#Simple ATM Cash Withdrawal Simulation
'''
Write a program to simulate an ATM cash withdrawal.
The program should take the withdrawal amount as input and verify its validity based on the available ATM balance
 and withdrawal rules.

The withdrawal amount must be a multiple of 100.
The withdrawal amount must not exceed the available balance. 
The withdrawal amount must be greater than zero.
***If all conditions are met, deduct the amount from the balance and print the remaining balance. 
Otherwise, print the appropriate error message.
Input Format:
A single integer representing the withdrawal amount. Decimal or floating-point numbers are not accepted.
''' 
# Available balance in the ATM
balance = 2000

# Taking input
withdrawal_amount = int(input())
def atm_withdraw(amount, balance):
    if withdrawal_amount <=0:
        return "Error: Invalid withdrawal amount"
    elif withdrawal_amount%100!=0:
        return "Error:Amount must be a multiple of 100"
    elif withdrawal_amount > balance:
        return "Error: Insufficient funds"
    else:
        New_balance = balance - withdrawal_amount
        return "Transaction successful.Remaining balance:",New_balance

# Print the output
result = atm_withdraw(withdrawal_amount, balance)
print(*result)
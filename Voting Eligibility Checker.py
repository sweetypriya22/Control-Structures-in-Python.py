#Voting Eligibility Checker

'''
Write a function 'is_eligible_to_vote(age, citizenship)' that determines whether a person is eligible to vote.

The function should consider two factors:

 The person's 'age' must be 18 or older. 
The person must be a citizen (indicated by a Boolean or string, where `True` or "Yes" means a citizen, and `False` or "No" means not a citizen).


The function should return `True` if both conditions are met, otherwise return `False`.



Input Format:

Two inputs:

`age` (a positive integer) 
 `citizenship` (a Boolean or string representing citizenship status).
Output Format:

The function should return a Boolean value: `True` if the person is eligible to vote, `False` otherwise.



Constraints:

 `age` is a Positive Integer.
`citizenship` can be a Boolean (`True` or `False`) or a String (`"Yes"` or "No").
Ensure that the input is “Yes” or “No” format only
'''
# Taking input
age = int(input())
citizenship_input = input()

def is_eligible_to_vote(age, citizenship):
    # Write your code
    if age<18 or not citizenship:
        return False
    else:
        return True

# Convert citizenship input to boolean without using string methods
if citizenship_input == "Yes":
    citizenship = True
elif citizenship_input == "No":
    citizenship = False
elif citizenship_input == "True":
    citizenship = True
elif citizenship_input == "False":
    citizenship = False
else:
    # If input is unexpected, treat as False
    citizenship = False
    
# Print the output
print(is_eligible_to_vote(age, citizenship))
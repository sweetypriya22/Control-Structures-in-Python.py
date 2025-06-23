#Movie Ticket Price by Age & Showtime
'''
Write a program to calculate the price of a movie ticket based on the customer's age and the showtime.



The Pricing Rules are:

Children (age < 12):
Ticket costs 5 regardless of showtime.
Seniors (age >= 60):
Ticket costs 7 regardless of showtime.
Adults (age 12 to 59):
Matinee shows (before 5 PM):10
Evening shows (5 PM or later): 12
'''

# Input Format:
# The first line contains an integer representing the age of the customer.      
# The second line contains an integer representing the showtime in 24-hour format (0 to 23).
# Output Format:
# Print the price of the movie ticket based on the age and showtime.
# Taking inputs
age = int(input())
show_hour = int(input())

def calculate_ticket_price(age, show_hour):
    # Write your code here
    if age < 12:
        price = 5
    elif age >= 60:
        price = 7
    else:
        if show_hour < 17:
            price = 10
        else:
            price = 12
    return price


# Print the output     
print(calculate_ticket_price(age, show_hour))
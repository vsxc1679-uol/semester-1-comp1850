"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Freddie Ash
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
unconfirmed = True
while unconfirmed:
    try:
        monthly = int(input("Please ener the amount you want to save monthly:"))
    except:
        print("Please ensure you enter an integer")
    else:
        unconfirmed = False
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
annualTotal = monthly * 12
# print this out for the user with a suitable message.
print(f"You will have saved £{annualTotal} by the end of the year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
finalAnnualTotal = annualTotal * 1.008
# print this out in the format £X.XX (to two decimal places).
print(f"With interest you would've saved £{"%.2f" % finalAnnualTotal}")

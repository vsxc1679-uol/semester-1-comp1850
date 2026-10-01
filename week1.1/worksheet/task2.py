"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Freddie Ash
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

try:
    monthly = int(input("Please ener the amount you want to save monthly:"))
except:
   print("Please ensure you enter an integer!")
else:    
    annualTotal = monthly * 12
    print(f"You will have saved £{annualTotal} by the end of the year")
    finalAnnualTotal = annualTotal * 1.008
    print(f"With interest you would've saved £{"%.2f" % finalAnnualTotal}")


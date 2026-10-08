# Worksheet 1.2: Task 1 Solution
import sys

mark = input("Please input the grade:")
try:
    mark = int(mark)
    if not(0 <= mark <= 100):
        sys.exit("Error: Grade must be an integer between 0 and 100")        
    if (0<=mark<40):
        print(f"{mark} is a Fail")
    elif (40<= mark <70):
        print(f"{mark} is a Pass")
    else:
        print(f"{mark} is a Distinction")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")


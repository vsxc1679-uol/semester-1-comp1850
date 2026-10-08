# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()
mean = 0
i = 0
for i in range(len(numbers)):
    mean = mean + numbers[i]
mean = mean / len(numbers)
if len(numbers) % 2 == 0:
    median = ((numbers[len(numbers)//2] + (numbers[(len(numbers)//2) - 1])) / 2)
else:
    median = numbers[(len(numbers)//2)]

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {mean}")
print(f"Median = {median}")
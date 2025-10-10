import re

s = "I bought 7 nuts for 6$ and 10 bolts for 3$."

numbers = re.findall('\d+', s)

print(numbers)  # ['7', '6', '10', '3']
# 71. Write a Python program to insertion at the beginning in OrderedDict.

from collections import OrderedDict

# Create OrderedDict
od = OrderedDict()
od['b'] = 2
od['c'] = 3

# Insert at beginning
od.update({'a': 1})

# Move 'a' to beginning
od.move_to_end('a', last=False)

print(od)

# 72. Write a Python program to check order of character in string using OrderedDict().

from collections import OrderedDict

# Function to check order of characters
def check_order(string, pattern):
    
    # Create OrderedDict from string
    dict = OrderedDict.fromkeys(string)

    ptrlen = 0

    # Check characters in order
    for key, value in dict.items():
        if key == pattern[ptrlen]:
            ptrlen = ptrlen + 1

        # If all characters matched
        if ptrlen == len(pattern):
            return True

    return False


string = "engineers rock"
pattern = "egr"

if check_order(string, pattern):
    print("Pattern is in order")
else:
    print("Pattern is not in order")


# 73. Write a Python program to sort Python Dictionaries by Key or Value.

# Dictionary
my_dict = {'c': 3, 'a': 1, 'b': 2}

# Sort by key
sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)

# 74. Write a program that calculates and prints the value according to the given formula:


import math

C = 50
H = 30

# Input values
values = input("Enter numbers separated by comma: ")

# Split values
D = values.split(',')

result = []

# Apply formula
for i in D:
    Q = math.sqrt((2 * C * int(i)) / H)
    result.append(str(round(Q)))

# Print result
print(",".join(result))



# 75. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
# array. The element value in the i-th row and j-th column of the array should be i*j.


# Input rows and columns
X = int(input("Enter number of rows: "))
Y = int(input("Enter number of columns: "))

# Create 2D array
array = []

for i in range(X):
    row = []
    
    for j in range(Y):
        row.append(i * j)
    
    array.append(row)

# Print array
print(array)


# 76. Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.


# Take input
words = input("Enter words separated by comma: ")

# Convert string into list
word_list = words.split(',')

# Sort words alphabetically
word_list.sort()

# Convert list into comma-separated string
result = ",".join(word_list)

# Print result
print(result)


# 77. Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically.


# Take input
words = input("Enter words: ")

# Split words into list
word_list = words.split()

# Remove duplicates using set()
unique_words = set(word_list)

# Sort words alphanumerically
sorted_words = sorted(unique_words)

# Print result
print(" ".join(sorted_words))


# 79. Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:

# Take input
sentence = input("Enter a sentence: ")

letters = 0
digits = 0

# Check each character
for ch in sentence:
    
    if ch.isalpha():
        letters += 1
        
    elif ch.isdigit():
        digits += 1

# Print result
print("Letters:", letters)
print("Digits:", digits)


# 80. A website requires the users to input username and password to register. Write a
# program to check the validity of password input by users. Following are the criteria
# for checking the password:


import re

password = input("Enter password: ")

# Rules
length_ok = len(password) >= 6 and len(password) <= 12
lower_ok = re.search("[a-z]", password)
upper_ok = re.search("[A-Z]", password)
digit_ok = re.search("[0-9]", password)
special_ok = re.search("[$#@]", password)

# Check validity
if length_ok and lower_ok and upper_ok and digit_ok and special_ok:
    print("Valid Password")
else:
    print("Invalid Password")



# 81. Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.


# Class with generator function
class DivisibleBySeven:
    
    def __init__(self, n):
        self.n = n

    # Generator method
    def generate(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i


# Take input
n = int(input("Enter value of n: "))

# Create object
obj = DivisibleBySeven(n)

# Print numbers divisible by 7
for num in obj.generate():
    print(num)

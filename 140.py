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


# 82. Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically. Suppose the following input is
# supplied to the program:


# Take input
sentence = input("Enter sentence: ")

# Split sentence into words
words = sentence.split()

# Create dictionary
freq = {}

# Count word frequencies
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort by key
sorted_freq = dict(sorted(freq.items()))

# Print result
for key, value in sorted_freq.items():
    print(key, ":", value)


# 83. Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")


m = Male()
f = Female()

m.getGender()
f.getGender()   


# 84. Please write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!".

import zlib

# Original string
text = "hello world!hello world!hello world!hello world!"

# Compress
compressed = zlib.compress(text.encode())

# Decompress
decompressed = zlib.decompress(compressed).decode()

print("Compressed:", compressed)
print("Decompressed:", decompressed)

# 86. Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check middle element
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    return -1  # Not found


# Example sorted list
arr = [1, 3, 5, 7, 9, 11, 13]

# Input target
target = int(input("Enter number to search: "))

# Call function
result = binary_search(arr, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")



# 87. Please write a program using generator to print the numbers which can be divisible
# by 5 and 7 between 0 and n in comma separated form while n is input by console.


# Generator function
def generate_divisible(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


# Input from user
n = int(input("Enter value of n: "))

# Collect results from generator
result = generate_divisible(n)

# Print comma-separated output
print(",".join(map(str, result)))


# 88. Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.

# Generator function
def generate_even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Input from user
n = int(input("Enter value of n: "))

# Collect results from generator
result = generate_even(n)

# Print comma-separated output
print(",".join(map(str, result)))



# 89. The Fibonacci Sequence is computed based on the following formula:


# Input number of terms
n = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1

# Print Fibonacci series
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 90. Assuming that we have some email addresses in the
# "
# username@companyname.com
#  (mailto:username@companyname.com)" format,
# please write program to print the user name of a given email address. Both user
# names and company names are composed of letters only.



# Take email input
email = input("Enter email address: ")

# Extract username
username = email.split("@")[0]

# Print username
print("Username:", username)


# 91. Define a class named Shape and its subclass Square. The Square class has an init
# function which takes a length as argument. Both classes have an area function which
# can print the area of the shape where Shape's area is 0 by default.


# Base class
class Shape:
    
    # Default area function
    def area(self):
        return 0


# Subclass
class Square(Shape):
    
    # Constructor
    def __init__(self, length):
        self.length = length

    # Area function
    def area(self):
        return self.length * self.length


# Create object
square = Square(5)

# Print area
print("Area of Square:", square.area())


# 92. Write a function that stutters a word as if someone is struggling to read it. The first
# two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.


# Function to create stutter word
def stutter(word):
    first_two = word[:2]
    return first_two + "... " + first_two + "... " + word + "?"


# Input word
word = input("Enter a word: ")

# Print result
print(stutter(word))


# 93. Create a function that takes an angle in radians and returns the corresponding angle
# in degrees rounded to one decimal place.


import math

# Function to convert radians to degrees
def radians_to_degrees(radian):
    degrees = radian * (180 / math.pi)
    return round(degrees, 1)


# Input
radian = float(input("Enter angle in radians: "))

# Output
print("Angle in degrees:", radians_to_degrees(radian))


# 94. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2
# elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a
# Curzon number.


# Function to check Curzon number
def is_curzon(num):
    
    # Formula check
    if (2 ** num + 1) % (2 * num + 1) == 0:
        return True
    else:
        return False


# Input
num = int(input("Enter a number: "))

# Output
if is_curzon(num):
    print(num, "is a Curzon number")
else:
    print(num, "is not a Curzon number")


# 95. Given the side length x find the area of a hexagon.


import math

# Function to calculate area of hexagon
def hexagon_area(x):
    area = (3 * math.sqrt(3) * (x ** 2)) / 2
    return round(area, 2)


# Input
x = float(input("Enter side length: "))

# Output
print("Area of hexagon:", hexagon_area(x))


# 96. Create a function that returns a base-2 (binary) representation of a base-10 (decimal)
# string number. To convert is simple: ((2) means base-2 and (10) means base-10)
# 010101001(2) = 1 + 8 + 32 + 128.


# Function to convert decimal to binary
def decimal_to_binary(num):
    return bin(num)[2:]


# Input
num = int(input("Enter a decimal number: "))

# Output
print("Binary representation:", decimal_to_binary(num))


# 97. Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.


# Function to find sum of numbers divisible by c
def divisible_sum(a, b, c):
    total = 0

    for i in range(a, b + 1):
        if i % c == 0:
            total += i

    return total


# Input
a = int(input("Enter start value: "))
b = int(input("Enter end value: "))
c = int(input("Enter divisor: "))

# Output
print("Sum:", divisible_sum(a, b, c))


# 98. Create a function that returns True if a given inequality expression is correct and
# False otherwise.


# Function to check inequality
def check_inequality(expression):
    return eval(expression)


# Input
expression = input("Enter inequality expression: ")

# Output
print(check_inequality(expression))


# 99. Create a function that replaces all the vowels in a string with a specified character.


# Function to replace vowels
def replace_vowels(text, char):
    
    vowels = "aeiouAEIOU"
    result = ""

    for letter in text:
        if letter in vowels:
            result += char
        else:
            result += letter

    return result


# Input
text = input("Enter a string: ")
char = input("Enter replacement character: ")

# Output
print(replace_vowels(text, char))


# 100. Write a function that calculates the factorial of a number recursively.

# Recursive function for factorial
def factorial(n):

    # Base condition
    if n == 0 or n == 1:
        return 1

    # Recursive call
    return n * factorial(n - 1)


# Input
num = int(input("Enter a number: "))

# Output
print("Factorial:", factorial(num))

# 101. Hamming distance is the number of characters that differ between two strings.


def hamming_distance(s1, s2):
    # strings must be same length
    if len(s1) != len(s2):
        return "Strings must be of equal length"

    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    return count


# Example
print(hamming_distance("karolin", "kathrin"))





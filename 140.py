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



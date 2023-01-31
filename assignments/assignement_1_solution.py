
# Start with this. Declare four string variables as follows.
# String is one of the data types in Python. It can be declared with single as well as double-quotation marks.
a = "Welcome"
b = "to"
c = "Python"
d = "!"

# Following should be the outputs printed on the command line. Use print() function.
# (Don't include tripple double-quotes. Tripple double-quotes can also be used as multi-line comment in Python.
# Similar to '#' symbol for single line comments. Python will ignore whatever is commented.)
# Note that there is no space between 'Python' and '!'.

# Output 1
"""
Welcome to Python!
"""

# Output 2. You can try printing this in single print() function as well :)
"""
Welcome
to
Python!
"""


# Solution:

# Suggestion: Keep some fixed spaces (or even no spaces) between symbols, variables etc.
# Decide your own set of aesthetic rules, just to make the code more organized.
# It doesn't matter to the computer, but it will make it easier for you to read your own programs in future :),
# especially effective for large programs.


# Output 1
print("Output 1:\n")

# Concatenate strings using '+' operator.
print(a + ' ' + b + ' ' + c + d)
# You can also store the concatenated variables in another variable and print it.
sentence = a + ' ' + b + ' ' + c + d
print(sentence)

# Use comma to separate the variables. Actually, this method first creates a list of variables and passes it to the print function.
# Elements of a list are printed separated by space. We will discuss lists in subsequent assignments. 
print(a, b, c+d)

# There is an optional parameter that you can pass to the print function.
# The 'end' parameter tells what to put at the end of the variable which is going to be printed.
# By default it is '\n' i.e. a new line character.
print(a, end=" ")
print(b, end=" ")
print(c, end="")
print(d)

##############################################################

# Output 2
print("\n####################################\nOutput 2:\n")

# Concatenate strings using '+' operator
print(a + "\n" + b + "\n" + c + d)

# I have put this just to put a black line between the two outputs.
print()

# The print function will put a new line after the variable which it has printed.
print(a)
print(b)
print(c, end="")
print(d)


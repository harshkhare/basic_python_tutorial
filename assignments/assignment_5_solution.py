
# In this assignment we are going to uderstand the flow control in Python.
# Flow control for an algorithm can be of two main types-
# 1. Conditional
# 2. Iterative
#
# 1. Conditional flow control
#    We can use if-else statements to control the flow of the algorithm based on a condition.
#    These conditions are like a bifurcation in the path, you select either of the two ways.
#    Remember that conditions usually evaluate to True or False, the behavior which we can
#    observe even in our daily lives. In Python, you could actually have a conditional statement
#    that generated a boolean output (True or False) or you couold have a statement which generates
#    an output which is numeric or even a string!
#    How does Python decide when the condition is not a boolean?
#    By convention any non-zero numeric value is considered True. This means that negative numbers
#    evaluate to True. In case of non-numeric values, everything evaluates to True.
#    There is one more way to denote False- the keyword 'None'. If any variable or object is assigned
#    a value of None, then it means that the variable/object does not exist. It has no associated memory
#    address to store it's value.

# One more thing to remember: Python needs proper indentation to designate blocks of code.
# For example statements to be executed if a condition is true are clubbed in a block and are shifted right
# by a fixed number of blank spaces. You can decide how many spaces or tabs you want to use, but that number
# should remain consistent. Two or four spaces are commonly used as an indent size. I prefer to use a single
# tab for each indentation.

# Ok, enough with the theory :)
# Here are some examples-

a, b, c = 1, 2, 3
if a == b:
	print(a,'is equal to',b)
else:
	print(a,'is not equal to',b)

if a != b:
	print(a,'is not equal to',b)


# Nested conditions
if a < b:
	if b < c:
		print("a < b < c") 

# In most cases nesting of conditions can be compressed using logical operator 'and'.
# There are other logical operators as well- 'or', 'not'
if a < b and b < c:
	print("a < b < c") 


# You can also check for presence of an object in a collection (list or dictionary)
number = 2134345
lotteryNumbers = [98375,923854,3746,938475,76143,98237,813423]
if number in lotteryNumbers:
	print("You have won the lottery!!!")


# Testing if a number is even or odd
d = 15
if d%2 == 0:
	print(d,'is even')
else:
	print(d,'is odd')
# Note: '%' is a modulus operator. It returns the remainder after division of two numbers.


# Let's write a fun program which tells whether or not to carry umbrella while leaving house today :)
# Let us assume only three types of weather conditions for simplicity- rain, clouds and sun
# So here's what we know about weather-
# If it is raining today, you obviously have to take umbrella with you. If there are clouds today, but it
# rained yesterday, then also you have to take umbrella. In any other case it might not rain and you
# need not carry an umbrella.
#
# Have a look at the program which uses a new construct 'elif' which translates to 'else if'
# This 'elif' is very handy way to write chained conditional flows.
yesterday = input("Yesterday's weather (rain/clouds/sun): ")
today = input("Today's weather (rain/clouds/sun): ")

if today == 'rain':
	print("Take umbrella")
elif today == 'clouds' and yesterday == 'rain':
	print("Take umbrella")
else:
	print("Do not take umbrella")

# Question:
# Could you modify the above program so that if user inputs anything other than rain, clouds or sun,
# then the program asks to put correct input?

# Solution:

# Version 1:
# This version avoids second input if the first input is wrong.
yesterday = input("Yesterday's weather (rain/clouds/sun): ")
if yesterday not in ['rain', 'clouds', 'sun']:
	print('Incorrect input for \'Yesterday\'s weather\'. Please choose from the set {rain, cloud, sun}')
else:
	today = input("Today's weather (rain/clouds/sun): ")
	if today not in ['rain', 'clouds', 'sun']:
		print('Incorrect input for \'Today\'s weather\'. PLease choose from the set {rain, cloud, sun}')
	elif today == 'rain':
		print('Carry Umbrella')
	elif today == 'clouds' and yesterday == 'rain':
		print('Carry Umbrella')
	else:
		print('No Umbrella required')


# Version 2:
# You can make the 'if' statement compact using 'or' between two conditions.
# But then it is not possible to show which input is wrong.
# It was possible in your solution.
yesterday = input("Yesterday's weather (rain/clouds/sun): ")
today = input("Today's weather (rain/clouds/sun): ")

if today not in ['rain', 'clouds', 'sun'] or yesterday not in ['rain', 'clouds', 'sun']:
	print('Incorrect input for \'Today\'s or Yesterday\'s weather\'. Please choose from the set {rain, cloud, sun}')
else:
	if today == 'rain':
		print("Carry umbrella")
	elif today == 'clouds' and yesterday == 'rain':
		print("Carry umbrella")
	else:
		print("Do not carry umbrella")


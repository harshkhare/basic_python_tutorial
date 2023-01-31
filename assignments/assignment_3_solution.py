
# There is another important data type- Boolean, which takes either of the two values, True or False.
# So it is possible to assign a True or False value to a variable as follows-
# a = True
# b = False
# Boolean values use only one bit in computer's memory. So they are highly memory efficient.
#
# There are some functions in Python which evaluate the input arguments and return either True or False.
# One such function is 'isinstance()'.
# It is useful to check whether or not a data type of a given variable is str or int or float or whatever.
# Find out the syntax of this function from this official python documentation- https://docs.python.org/3/library/index.html
# Look under Built-in Functions.
# 
# This function, isinstance(), is very useful in some programs where you do not know
# the type of variable which you might have obtained from another running program.
# You might not face this situation so soon, but good to know :)

# Question 1:
# Print only integers from the following variables.
# Notice the how you can assign values to many variables in one line!
a, b, c, d, e, f = "Sampada", 1.5, "5", "Harsh", 4, "45.4"

# Solution:
for v in a,b,c,d,e,f:
	if isinstance(v, int):
		print(v)

# Additional information: There a function called type() which tells you the data type of any given variable.
# Have a look at it.

#########################################################################################

# Type casting: This is something you have already used in your answer to the assignment 2.
# You can convert int or float type into str as follows-
# a = 12.456
# print("Type casted to string" + str(a))
# Notice that now we can concatenate it with other strings.
# Similarly you can use float(), int() to type cast variables.

# This brings us to string formatting.
# Let's go into little more details of string formatting.
# We are going to leverage your answer to the assignment 2.

"""
pi = 22/7
radiusEarth = 6400 
lat_np = 90

city_name = input('Enter the name of the city : ') 
lat_city = float(input('Enter the latitude of the city : '))

lat_diff_input = lat_np - lat_city 
ang_rad_diff_input = (pi * lat_diff_input) / 180
arc_length_input = radiusEarth * ang_rad_diff_input

# Here's where we are going to print in a slightly different way.
# We are going to format the strings such that numeric variables are displayed as we want.
print("The distance to the North pole from %s is %f km" % (city_name, arc_length_input) )
print('The distance to the North pole from ' + city_name + ' is ' + '{:1.6f}'.format(arc_length_input) + ' km')
"""

# Note the format() function. '{:.2f}' tells the function to keep only 2 decimal places in the float.
# In fact, the format() function is very flexible. Have a look at this web page to see what all you can do with it.
# https://pyformat.info/

# Question 2:
# Following numbers are rows of a matrix. Print this matrix so that it looks pretty :)
# Something like this-
#
#    0.123  4.000   2.457
#    2.000 -4.000  56.700
# 1234.400 34.000 -23.233
#
# Or decide your own format, but it should be nice to look at!

a11, a12, a13 = 0.1233, 4, 2.45677
a21, a22, a23 = 2, -4, 56.7
a31, a32, a33 = 1234.4, 34, -23.233

# Solution:

print("{:10.3f} {:10.3f} {:10.3f}".format(a11, a12, a13))
print("{:10.3f} {:10.3f} {:10.3f}".format(a21, a22, a23))
print("{:10.3f} {:10.3f} {:10.3f}".format(a31, a32, a33))

# The format {:10.3f} translates to this-
# Use total 10 character width with 3 digits after decimal place.
# So a number would look something like this-
# xxxxxx.xxx

print("\nAlternate way")
print('{:10.3f}'.format(a11)+" "+'{:10.3f}'.format(a12)+" "+'{:10.3f}'.format(a13))
print('{:10.3f}'.format(a21)+" "+'{:10.3f}'.format(a22)+" "+'{:10.3f}'.format(a23))
print('{:10.3f}'.format(a31)+" "+'{:10.3f}'.format(a32)+" "+'{:10.3f}'.format(a33))

# Another example
print("\nAnother example")
print("{:6d} {:6d} {:6d} {:6d}".format(1, 1**2, 1**3, 1**4)) 
print("{:6d} {:6d} {:6d} {:6d}".format(3, 3**2, 3**3, 3**4)) 
print()

# If you have noticed, we used 'f' for floats and 'd' for integers. For strings one can use 's'.
#
# String formatting in Python is very very flexible and there could be more than one ways to do the same thing!
# In a way, this is good. But sometimes it might just become too much to remember.
# So my suggestion is that you need not remember all possible ways. Over time you will acquire understanding for it.
# (And even then there could be something new which you will see for the first time in some code :P)

#######################

# Comments: One new thing introduced here is the '.' symbol before the format() function.
# This comes from the concept of object oriented programming.
# We do not need to go into too many details at this moment.
# In simple words, any variable can have different types of functionalities (or methods).
#
# Let's see an analogy. Let us say we have a hypothetical data type called 'human'.
# So you can create a variable of type 'human'. Let us say the name of that variable is 'sampada'.
# In programming terms we say- 'sampada' is an instance of 'human'.
# If you do type(sampada), you will get output <class 'human'>. Remember the type() function?
#
# Now ask a question, 'What all can sampada do?'.
# The variable 'sampada' is of type 'human', so 'sampada' can do everything that is defined for 'human'.
# These actions are defined as, for example, walk(), run(), swim(), eat() etc.
# The way we call for those actions is like this-
# sampada.walk()
# sampada.swim()
#
# Except for built-in functions of Python (like print(), type() etc.),
# all other functions associated with different types of variables are called methods of those types of variables.
# They are always called with a '.' after the variable name.





# In the beginning of assignment 7, we talked about making our application more functional and error-proof.
# Two things are essential to achieve this. First is defining our own functions for special tasks so that the
# code becomes non-redundant and well organized. We covered this part in the assignment 7.

# The present assignment deals with the second important thing, which is about consciously handling run-time errors.

# What are run-time errors?
# You might have noticed that some of your codes exit with an error like ValueError, IndexError, KeyError etc.
# These errors occur at a certain step in the code and the Python interpreter terminates the code without executing
# the remaining steps. Such errors are different from syntax errors. They occur only when the code starts running.
# The Python interpreter doesn't have any way to identify if and when such errors will happen before the program actually runs.

# The names of such errors suggest what type of error the Python interpreter might have faced while running the code.
# So you might have got an idea about what causes such errors. Let us see an example to make it clear.

mylist = ['a','b','c']
#print(mylist[5]) # I have commented this line because it will cause an error. Try uncommenting it.
print("\n\n")

# If you run the above code, Python will print following error message and the code will.

# Traceback (most recent call last):
#   File "assignment_8.py", line 36, in <module>
#     print(a[5])
# IndexError: list index out of range

# Since this error occurred while accessing the index 5 of 'mylist', that particular statement will not execute and
# the code will exit. The Python interpreter says that it has found an 'IndexError' and then gives
# a short explanation 'list index out of range'. This means that we have tried to access a non-existent index in the list.
# You can see that there is no way for the python interpreter to predict this error with certainty before the program runs.

# You might argue that from the previous line, the Python interpreter should have understood that there are only
# 3 elements in the list. Then if it sees 'mylist[5]' written on the next line, why can't it tell that there is
# going to be an error?
# The answer is that this looks an obvious error because it is a very very simple code. Most real codes are
# almost never as simple as this one. There could be several steps through which this list could be modified before
# it's elements are accessed. Or there could be other codes modifying the same list simultaneously.
# The point is that the design of the Python interpreter has to be generalized to address all such possibilities.
# Therefore, it makes sense to categorize such errors as run-time errors.

########################################################################################


# Although these errors do not show up unless they happen, the Python interpreter provides a systematic way to
# handle such incidences.

# The method is very analogous to the way we deal with situations in our day-to-day life.
# Suppose you are crossing a street. Let's say you took a first step into the street. What might happen with this step?
# 1. There will be no vehicles coming your way.
# 2. There will be one/more vehicles coming your way, but they are far away.
# 3. There will be one/more vehicles coming your way and they are so close that you will get hit.

# There is no issue with the first and the second situation. But the third situation will lead to something similar to
# exiting the code :P
# Important question is, what do you do if you see that your step leads to the third situation which is an error in
# the task of crossing the street. You will definitely step back and look for other options.

# Let us write this algorithm of street crossing in a pythonic pseudo-code.

# while(street_not_crossed):
# 	look_in_the_street()
# 	try:
# 		step_forward_and_look_again()
# 	except:
# 		step_backward()
# 		shout("Oops! Just saved!!!!")
#
# shout("Yessss! I crossed the street!!!")

# What we are doing is, we are trying to do an action and if we judge that there is some problem with it, we do another action.
# The 'try' and 'except' keywords help in this type of control.
# The Python interpreter tries to run whatever is in the 'try' block. If there is no error, it will ignore the 'except' block.
# If any error occurs in the 'try' block, then the lines in the 'except' block are executed.

########################################################################################


# Apart from 'try' and 'except', there is one more keyword that can follow the 'try' keyword. It is called 'finally'.

# To make things more clear, see how these error handling protocol is also present in human language.
# In human terms, the 'try', 'except' and 'finally' would be used something like this in a sentence-
#
# Try to do this, except this happens or this happens, and finally do this.

# You might omit 'except' or 'finally' in some cases-
#
# Try to do this, except this happens or this happens.
# Try to do this, and finally do this.

# One more realistic example-
# Try to insert the thread in the needle-hole, except the thread is not in the hole or except the thread is bifurcated, and finally tie a knot.

# See this real example as well :) :P-
# Try preparing assignment-8, except packers-movers do not call, finally send assignment-8 to Sampada.

# Due to this analogous structure to human language, sometimes 'try', 'except' and 'finally' are also called clauses.

########################################################################################


# Here's one more example.

import sys

try:
	print("Inside \'try\' block")
	number = float(input("Please type a number (integer or float): "))
	print("Square of",number,"is",number**2,"\n")
except:
	print("Inside \'except\' block")
	print("Error type:",sys.exc_info()[0],"\n")

print("Further lines of code will be executed hereafter.\n")

# The error is first encountered in the line where we convert the input to float.
# However, the code does not exit at this line even if error occurs. Instead, it directly jumps to the 'except' block.
# After executing lines in the except block, it continues with the rest of the code.
# Without 'try' and 'except' structure, the code would have exited throwing an error if the input was non-numeric.

# Note that we have imported a 'sys' module which is used to get the type of exception.
# 'sys.exc_info()' function returns the information about the most recent exception that has occurred.

########################################################################################


# Catching specific exceptions
# As you saw, different errors are named differently.
# It is possible to catch them separately and do something different for each type of error.
# Python supports this by allowing multiple 'except' clauses for one 'try' clause.
# General syntax for doing this goes as given below.

try:
   # do something
   pass
except ValueError:
   # handle ValueError exception
   pass
except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass
except:
   # handle all other exceptions
   pass

# Note: We have written 'pass' keyword in the blocks as it works as a place holder when we do not want do anything.

# What is happening in the above example is that, first we will try to do something.
# Then if a 'ValueError' occurs, we jump to the first 'except' clause.
# If either 'TypeError' or 'ZeroDivisionError' occurs, we jump to the second except clause.
# And if any other error occurs, we jump to the third (i.e. the last) 'except' clause.

########################################################################################


# Raising exceptions
# Exceptions are automatically raised when errors occur at run time.
# But we can forcefully raise an exception using the keyword 'raise'.
# We can also optionally pass in a value to the exception to clarify why that exception was raised.

try:
	a = int(input("Enter a positive integer: "))
	if a <= 0:
		raise ValueError("That is not a positive number!")
except ValueError as ve:
	print(ve)

print("\n\n")

# Here's the output of the above piece of code-
# Enter a positive integer: -2
# That is not a positive number!

# We have raised a 'ValueError' manually and we have also told the Python interpreter to
# print 'That is not a positive number!' on the command line.

# The 'as' keyword in the line 'except ValueError as ve:' creates a variable name 've' which holds the specified error.

########################################################################################


# Using the 'finally' clause
# The 'finally' clause is generally used to make sure that resources are released once the task is completed.
# This could be deleting unnecessary variables, closing files opened for some purpose, disconnecting from server etc.

try:
	biglist = [1,2,3,4,5,6,7,8]
	# Do something with the list- a mathematical operation, searching etc.
	print("Doing something with biglist...\n")
finally:
	del(biglist)
	print("biglist is deleted.\n")

print(biglist)
print("\n")

# Note: The in-built function 'del' deletes a variable. You can see that a 'NameError' is thrown if you try to use
# the variable 'biglist' once it is deleted,

# Question:
# You saw that 'print(biglist)' written above makes the code exit with a 'NameError'. Can you handle it in a nice way?



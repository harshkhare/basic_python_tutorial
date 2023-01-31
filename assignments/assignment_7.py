
# We designed a simple command-line calculator application in the assignment 6.
# In next few assignments, we will develop it further by adding more functionality and
# making it more error proof.

# For adding more functionality, we need to understand how to design our own functions for each task,
# so that we can avoid unnecessary repetitions in the code.

# For making the code error proof we need to do better error handling. Here we are concerned with
# the run-time errors. These errors occur due to an incompatible value getting generated somewhere
# in the code. For example, you want to convert user input to an integer, but there is a letter in the
# user provided input. This will raise an error and the code will exit. Python provides elegant ways of
# handling such run-time errors.


##################################################################################################

# In this tutorial we will see how to design our own functions.

# Most commonly, a function has four main parts.
# 1. Name
# 2. Parameters
# 3. Body
# 4. Return value

# If you notice, this much like the mathematical concept of function.
# What does it convey to you when you write 'sin(90)'?
# (We sometimes omit the brackets, but nonetheless we provide a number to the sine function.)
# 1. Name: sin (Short form of sine)
# 2. Parameter: 90
# 3. Body: What do you do with '90', the parameter? You might want to look into ways of calculating sine of an angle from scratch :)
# 4. Return value: What do you get back? It is sine of 90, which is 1.

# Now, calculating sine of an angle from scratch might be complicated.
# So we will write a function for a very simple task.
# Here's how we define a function in Python.

def say_hi():
	print("Hi")

# The keyword 'def' tells Python that a definition of a new function is starting.
# In this case 'say_hi' is the name of the function. The body contains only 'print("Hi")'.
# Whatever is in the body of the function is shifted by one indent to right, making it a code block.
# Note that there are no parameters given as nothing else is reuired to do what this function does.

# You can call this function as follows.

say_hi()
print("\n\n")

# We have not yet talked about the return value of this function. Let's find out what this function is returning by default.

r = say_hi()
print(r)
print("\n\n")

# Or you can simply write 'print(say_hi())'.

# The function returns 'None', which literally means 'nothing'.

# Let us now modify the function to return some value. You can return any type of variable- int, float, string, list, dictionary etc.

def say_hi():
	print("Hi")
	return(1)

r = say_hi()
print(r)
print("\n\n")

# Returning 1 in this function doesn't really mean anything, but we can return useful values as shown below.

def addTwoNums(a,b):
	return(a+b)

print(addTwoNums(2,5.6))
print("\n\n")

# One more point to note: If a function needs more than one parameters, separate them by commas in
# the function definition and provide them in the same way when calling the function.


##################################################################################################

# Note: Parameters vs arguments, when to say what.
# When we define a function, we declare 'parameters' of the function.
# When we call a function, we provide 'arguments' to the function.


##################################################################################################

# Examples of more complicated parameters

def process_list(mylist,a):
	# This function squares each number in the list and adds given number to each element and then returns the modified list.
	newlist = []
	for element in mylist:
		newlist.append(element**2 + a)
	return(newlist)

print(process_list([1,2,5,4,3],3))
print("\n\n")

# Lists are mutable, i.e. you can make changes in a list. So, rather than wasting more memory for a new list,
# you can do something like this.

def process_list(mylist,a):
	# This function squares each number in the list and adds given number to each element and then returns the modified list.
	for i in range(0,len(mylist)):
		mylist[i] = mylist[i]**2 + a
	return(mylist)

print(process_list([1,2,5,4,3],3))
print("\n\n")


##################################################################################################

# Below is an interesting code- a simple implementation of the bubble sort algorithm.

def bubble_sort(mylist):
	length = len(mylist)
	for i in range(0,length):
		for j in range(i,length):
			#print(i,j)
			if mylist[i] > mylist[j]:
				# Swap i'th and j'th elements of mylist
				e = mylist[i]
				mylist[i] = mylist[j]
				mylist[j] = e
	return(mylist)

some_list = [2,5,4,23,6,8,3]
print("Original list",some_list)
sorted_list = bubble_sort(some_list)
print("Sorted list",sorted_list)
print("\n\n")


##################################################################################################

# Calling one function from another function

def func2(x):
	print("I am inside func2. You passed",x,"to me.")

def func1(x):
	print("I am inside func1. You passed",x,"to me.")

	print("Calling func2.")
	func2(x+1)

func1(5)
print("\n\n")

# Did you notice that we have named the parameter of both the functions 'x'?
# Why doesn't Python get confused between the variables of same name, and still print different values?
# This is because Python determines the scope of different variables.
# Variables with same name but in different scope are always kept separate.
# In case of function parameters, those variables are limited to that function alone.
# So the same name in the parameters of different functions does not create any confusion.
# Such variables, declared as parameters of a function, live within the body of that function and die when the function returns.


##################################################################################################

# Now you can easily modify your calculator code using the concept of functions.
# It might not look like a big deal, because the tasks we are doing are quite simple. But with more complicated
# tasks, functions become very handy.
# You can define it once and call it again and again without having to write the same task everywhere.
# Correcting mistakes also becomes easier, as you have to make corrections only in one place :) :P


##################################################################################################

# Question 1:
# Modify your calculator code by writing your own functions for different operations- +,-,*,/.

##################################################################################################

# Question 2:
# Write functions for following tasks-
#
# Note: Writing the functions for these tasks is more important. Do not focus on taking user input.
# First get the functions ready and then deal with the user input.
#
# 1. Average
#
# 2. Standard deviation
#    Hint: You can call another function from within this function. Make use of your 'average' function.
#
# 3. Varience
#
# 4. Scalar product (or dot product) of two vectors
#    Hint: You need to take two lists as parameters. Each list represents coefficients of a vector.
#          Example- Let us consider two points in 3D space, P = [3,2,4] and Q = [1,2,1]
#          The scalar product P.Q is 3*1 + 2*2 + 4*1 = 11.
#          In your implementation, try not to restrict the length of vectors.
#
# 5. Vector product (or cross product) of two vectors
#    Hint: You need to return a vector (i.e. a list)




# As mentioned in the beginnign of the assignment 5, there are two main types of flow control.
# 1. Conditional
# 2. Iterative

# We covered the basics of conditional flow control in the assignment 5.
# Here, we are going to cover the iterative flow control, which includes 'for' and 'while' loops.

# In general any loop requires two pieces of information-
# 1. Condition to decide whether to repeat the process
# 2. End condition to decide whether to stop repetitions


############################################################################################################

# The 'while' loop:
# The 'while' loop tells the algorithm to repeat certain steps till some condition is true.
# Therefore, it is very important make sure that the condition becomes false sometime, otherwise
# the code will run infinitely. It will get stuck in the loop.
# Of course, if you really want the code to run infinitely (i.e. till the computer is ON), then
# 'while' loop could be a simplest way to go. Examples of such applications include background
# services for graphics, sound, microphone, network etc.
# Or you can also write a simple yet very annoying virus code with infinite loops :P

# Before we go on with examples, here's something you should avoid writing unless you are fully
# aware of why you are doing so. This will go into an infinite loop.
#
# while(True):
# 	<do something>
#
# If you ever encounter your program stuck, you can try pressing Ctrl+C to break the code.
# Another way is to kill the process associated with your stuck code.
# Open another terminal window. Then type 'top' and hit enter.
# The 'top' command will give you the list of all running processes sorted by CPU usage.
# The left most number is the process ID (or PID).
# Identify the process for your stuck program. Note down the PID.
# Then press 'Q' button to exit the 'top' command.
# Then use the kill command to kill the identified process as follows.
# kill <PID>


# Now let us start with the examples.
#
# Any expression that yields a logical value (True/False) can be given to the 'while' loop.
# Note that we have initialized 'i' before the loop begins and 'i' is incremented in each loop iteration.
# In this way, we are avoiding going into an infinite loop.
# Always remember to put some loop breaking step inside a 'while' loop.
i = 0
while i < 7:
	print(i,"is less than 7.")
	i += 1
print(i," is not less than 7.\n\n")

# You can also write- 'while(i < 7):'.
# The brackets around the condition are optional in Python.

# The following condition tests whether 'i' is in the given list (or any collection like tuple, dictionary etc.)
# Again note that 'i += 1' avoids infinite loop.
i = 0
while i in [0,1,2,3,4,5,6,7]:
	print(i,"is in the list.")
	i += 1
print(i," is not less than 7.\n\n")


############################################################################################################

# The 'for' loop:
# The 'for' loop is designed especially to work with collections (lists, dictionaries, tuples etc).
# The condition here is implicit. It fetches each element from the collection one by one and
# the implicit condition remains true until the collection is empty.

for i in [0,1,2,3,4,5,6,7]:
	print(i,"is in the list.")

# Note the difference between 'while' and 'for'.
# I case of the 'for' loop, neither did we initialize 'i' nor are we incrementing it inside the loop.
# This is because 'i' is already taking values of elements in the list. This is very safe because
# it is unlikely to go into an infinite loop, unless the collection itself is infinite.


############################################################################################################

# Breaking loops and not doing anything inside a loop
# The 'break' statement anywhere inside a loop will break the closest parent loop.
# The 'continue' stament anywhere inside a loop will ignore any more steps inside the loop and begin with the next iteration.
# The 'pass' statement can be written inside a loop do denote that you do not want to do anything inside the loop.

while(True):
	action = input()
	if action == 'exit':
		break
print("You broke the loop")

# See how you can avoid 'else' by using 'continue'
for i in range(0,10): # range() function generates numbers between given limits.
	if i <= 5:
		print("Number is",i)
		continue
	print("Limit exceeded.")
	print("Number > 5")

# This 'for' loop is lazy :), it does not want to do anything :P
for x in range(5,20):
	pass

############################################################################################################

# Here's a fun exercise.
# Given a text input, we can get counts for all the unique words.
# Note that tripple double quotation marks can be used to declare a multi-line string.
sentence = """Chandrayaan-2 is on a mission unlike any before. Leveraging nearly a decade of scientific research
and engineering development,India's second lunar expedition will shed light on a completely unexplored section
of the Moon — its South Polar region. This mission will help us gain a better understanding of the origin and
evolution of the Moon by conducting detailed topographical studies, comprehensive mineralogical analyses,
and a host of other experiments on the lunar surface. While there, we will also explore discoveries made by Chandrayaan-1,
such as the presence of water molecules on the Moon and new rock types with unique chemical composition."""

# The 'split()' method splits the string by spaces or blanks or new lines, and returns a list.
print(sentence.split())
print("\n\n")

my_dictionary = {}  # Initialize empty dictionary.
for word in sentence.split():
	if word not in my_dictionary:
		my_dictionary[word] = 0  # Initialize count to zero when the word is first encountered.
	my_dictionary[word] += 1  # Increment word count by one.

print("Word counts:")
for word in my_dictionary:
	print(word + ": " + str(my_dictionary[word]))
print("\n\n")


################ A little bit of diversion ################

# We spend less time on sorting of lists and dictionaries in previous assignments.
# Let us now do some sorting on keys as well as values of a dictionary.

# It's very easy to sort a dictionary on keys.
# Note how the capital and small letters are sorted. Capital letters always come before small letters.
print(sorted(my_dictionary))
print("\n\n")

# You can use sorted keys inside a loop.
# The 'keys()' method returns a list of keys, which can then be sorted.
# Similarly you can use 'values()' method to get values in the dictionary in a list format.
for word in sorted(my_dictionary.keys()):
	print(word + ": " + str(my_dictionary[word]))
print("\n\n")


# Problem comes when you want to sort a dictionary based on the values.
# For example when you want to find out the word with highest count in our example.

# There are many ways to do that. Here's one simple way.

# If you sort a list of tuples using the in-built 'sorted()' function, it will return you the list sorted based on
# the first element in each tuple.
my_list = [(1,"D"),(3,"A"),(0,"Q")]
print(sorted(my_list))
print("\n\n")

# We can leverage this to sort a dictionary based on values.
my_list = []
for word in my_dictionary:
	my_list.append( (my_dictionary[word],word) )

print(sorted(my_list, reverse=True))
print("\n\n")

# Following is a compressed version of what we just did :)
sorted_by_values = sorted([(value, key) for (key,value) in my_dictionary.items()], reverse=True)
print(sorted_by_values)
print("Word with highest count :", sorted_by_values[0][1], sorted_by_values[0][0])


############################################################################################################

# Question:
# Write a code for simple calculator application which can provide addition/subtraction/multiplication/division of integers.
# This is what it should be able to do-
# Ask the user to type an expression in the form: <integer1><space><operator><space><integer2>
# Then process this input to get two numbers and an operator. Depending upon the operator, print the output of the expression.
# Importantly, this program should not exit until the user types something like 'exit' or 'quit' as an input. (Remember infinite 'while' loops?)
# Make the program as user friendly as possible :)


Solution:

print("This is a simple calculator application which provides addition/subtraction/multiplication/division of  integers ", "\n")
print("Enter the expression in the folllowing format:  <integer1><space><operator><space><integer2>", "\n")

# Exit instruction 

print("You can quit the program by typing 'exit' or 'quit' ", "\n", "\n")


#include the line to check if input is correct else ask for correct input 

# Calculator begins. 
while(True): 				#This loop is so that the program doesn't stop till instructed 
	sentence = input('Enter the expression to be calculated :'  )			#Input 

	#This is to locate the position of the operator
	counter = 0 
	
	for i in range(0,len(sentence)):
		if sentence[i] == '+' or sentence[i] == '-' or sentence[i] == '*' or sentence[i] == '/' :
			counter = counter + i
			break


	### NEED TO CHECK IF INPUT IS CORRECT by checking integer part   		
	### See comments at the end of the code 
	### take input and synthesize it to give answer 
	
	# Program ends if instrcuted 
	if sentence == 'exit' or sentence == 'quit':
			break
	# Does the calculation as per the input operator 		
	elif sentence[counter]=='+':
		print(sentence, '=', int(sentence[0:counter]) + int(sentence[counter+1:]))
	elif sentence[counter]=='-':
		print(sentence, '=', int(sentence[0:counter]) - int(sentence[counter+1:]))
	elif sentence[counter]=='*':
		print(sentence, '=', int(sentence[0:counter]) * int(sentence[counter+1:]))
	elif sentence[counter]=='/':
		print(sentence, '=', int(sentence[0:counter]) / int(sentence[counter+1:]))
	else:	#If the operator part input is incorrect then instruts so 
		print(sentence, 'is', 'invalid input.', "\n")
		print('Please provide correct input in the following format : :  <integer1><space><operator><space><integer2> ') 
		
######################################################################################################################################


		
			



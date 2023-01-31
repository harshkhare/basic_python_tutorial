
# There are three common data structures (or collections) in Python.
# List, Tuple and Dictionary.
# Lists and dictionaries are much more commonly used than tuple.

########################################################################

# Lists:
# A list is a serially arranged collection of objects. It is similar to an array in C language.
# Index of list starts at zero. Length of a list can be theoretically infinite,
# only limited by the memory of your computer.

mylist = [34, 45, 12, 45, 23, 5, 7, 5, 4, 9, 10]
print(mylist)
print("First element:", mylist[0])
print("Second element:", mylist[1])

# 
print("Last element:", mylist[-1])
print("Second last element:", mylist[-2])

# Lists are mutable objects. You can make changes in them.
mylist[1] = 0
print(mylist)

# You cannot add an element to the list like this.
#mylist[5] = 1
# In the same way, you cannot access a nonexisting index of a list. 
#print(mylist[100])

# To add an element to the list, you have to use the append() method.
mylist.append(1)
print(mylist)
print(mylist[5])

# Length of the list
print(len(mylist))

# You can remove elements from the list.
mylist.pop()
print(mylist)

# This will pop out element at index 2 from the list.
mylist.pop(2)

# Note that the pop() method makes changes to the list that are irreversible.
# However, it returns you the element it removed and you can store it in another variable.

x = mylist.pop(4)
print(x)

# You should go through the official domumentation of python to get familiar with more methods of lists.
# https://docs.python.org/3/tutorial/datastructures.html


# Slicing of lists. This does not change the list. It just returns the slice of the list. Original list remains same.
mylist = [0,1,2,3,4,5,6,7,8,9,10]
print(mylist[2:4])
print(mylist)


print(mylist[:3])
print(mylist[5:])

# Question:
# Here's something funny. Explain what is happening with this syntax. What do these three numbers represent?
print(mylist[2:9:2])

# Solution:
# The three numbers represent-
# [start:end:step]
# Therefore mylist[2:9:2] fetches elements of mylist starting at index 2 till index 9 with a step of 2 i.e. alternate elements.


# Lists can contain differnt types of variables or ogjects.
srNo = 1
name = 'Harsh'
CGPA = 6.8
degreeAwarded = True

info = [srNo, name, CGPA, degreeAwarded]
print(info)
print(info[1] + " has received CGPA " + str(info[2]) + ".")

########################################################################

# Dictionaries
# Did you notice that even if we have a data structure to hold information of one person,
# we still have to remember which index of that list denotes what.
# But with dictionaries we get more flexibility. Dictionaries are similar to associated lists.
# There are key:value pairs. Duplicate keys are obviously not allowed, but values can repeat.
# The keys of a dictionary are unordered. In fact, there is no need for them to be ordered.
#
# We are going write like this-
# some_dictionary = {key1:value1, key2:value2, key3:value3}

info = {'SrNo':1, 'Name':'Harsh','CGPA':6.8, 'DegreeAwarded':True}
print(info)
print(info['Name'] + " has received CGPA " + str(info['CGPA']) + ".")


# How about storing data for multiple individuals in a single dictionary?
# Remember- Lists and dictionaries are collections of objects. So it is possible to have a dictionary of dictionaries!
# It is like a 2-dimensional array.
data = {'Sampada': {'SrNo':1, 'CGPA':7.3, 'DegreeAwarded':True},
				'Supriya': {'SrNo':2, 'CGPA':7.8, 'DegreeAwarded':True},
				'Anuja':   {'SrNo':3, 'CGPA':7.9, 'DegreeAwarded':True},
				'Sumedha': {'SrNo':4, 'CGPA':7.1, 'DegreeAwarded':True}}

print("\n")
print("Anuja's data\n", data['Anuja'],"\n")
print("Supriya's degree status:", data['Supriya']['DegreeAwarded'])


# Adding a key:value pair to a dictionary is easy.
# Do the following to add a blank dictionary as a value of the new key 'Harsh'.

data['Harsh'] = {}

# Of course, if you want to add a filled dictionary as a value, you can do so.

data['Harsh'] = {'SrNo':3, 'CGPA':7.9, 'DegreeAwarded':True}


# Question:
# Did you notice that Harsh and Anuja got same SrNo.
print(data['Harsh']['SrNo'], data['Anuja']['SrNo'])
# Also, the present data structure does not allow same name for two people.
# If you try to add a key:value pair for a new person with same name, it will just update the value of existing person with that name.
# Can you write this dictionary structure in a different way, so that duplications of the SrNos is avoided?

# Solution:
# Use SrNo as key.
data = {1: {'Name':'Sampada', 'CGPA':7.3, 'DegreeAwarded':True},
				2: {'Name':'Supriya', 'CGPA':7.8, 'DegreeAwarded':True},
				3: {'Name':'Anuja',   'CGPA':7.9, 'DegreeAwarded':True},
				4: {'Name':'Sumedha', 'CGPA':7.1, 'DegreeAwarded':True}}


# Some quick things. You will know what's happening here. No need for explanation.
print(data.keys())
print(data.values())
print(sorted(data.keys()))


# Question: Why does 'return' not work in the loop?

# This was the dictionary
data = {'Sampada': {'SrNo':1, 'CGPA':7.3, 'DegreeAwarded':True},
				'Supriya': {'SrNo':2, 'CGPA':7.8, 'DegreeAwarded':True},
				'Anuja':   {'SrNo':3, 'CGPA':7.9, 'DegreeAwarded':True},
				'Sumedha': {'SrNo':4, 'CGPA':7.1, 'DegreeAwarded':True},
				'Harsh':   {'SrNo':3, 'CGPA':7.9, 'DegreeAwarded':True}}

## This loop finds duplicates 

for i in data.keys():
 	for j in data.keys(): 
 		if i!= j and data[i]==data[j]:
 			print('Duplicate found for',i,' with', j)
 		else:
 			print('')  #Wonder why return didn't' work here 

# The 'return' statement is applicable for functions, not for loops or if-else conditions.
# Instead, you could use different keywords to control loop flows-

print("***************")
for i in data.keys():
 	for j in data.keys(): 
 		if i!= j and data[i]==data[j]:
 			print('Duplicate found for',i,' with', j)
 		else:
 			pass # The 'pass' keyword is used if you do not want to do anything in a code block. This keyword works for any code block, be it a function, loop or if-else.

for i in data.keys():
 	for j in data.keys(): 
 		if i!= j and data[i]==data[j]:
 			print('Duplicate found for',i,' with', j)
 		else:
 			continue # The 'continue' keyword is used to continue with the loop. It controls the closest parent loop, the loop for variable j in this case. This keyword is used to control loops only.

for i in data.keys():
 	for j in data.keys(): 
 		if i!= j and data[i]==data[j]:
 			print('Duplicate found for',i,' with', j)
 		else:
 			break # The 'break' keyword is used to break the loop. It controls the closest parent loop, the loop for variable j in this case. This keyword is used to control loops only.

print("\n***************")
########################################################################

# List comprehension for strings:
# This is really awesome way of handling strings. In python, you can directly consider strings as lists of characters.
# Then slicing of strings works in exactly the same way as it does for lists.

mystr = 'Welcome to Python!'

print(mystr)
print(len(mystr))
print(mystr[3])
print(mystr[-12:-3])
print(mystr[:2])
print(mystr[7:])
print(mystr[4:10])
print(mystr[::3])


# Question:
# How would you print a reversed string?
# !nohtyP ot emocleW
# Hint: You might want to think about mystr[::?] format. Replace ? with something.
# Remember- Same can be used to reverse lists.

# Solution:
print(mystr[::-1])
# This tells Python to take all indices of mystr and go with a step of 1 in opposite direction.

########################################################################

# Tuples
# A tuple is a list which is immutable. Once you create it, you cannot change its elements.
# This kind of behavior is useful when you are working with lists that should not change, such as-
# Days of week, list of possible grades etc.
# Notice that we use round brackets to declare a tuple. It is square brackets for list and curly brackets for dictionary.
grades = ('A','B','C')

print(grades)
print(grades[2])

# This will give error
# grades[0] = 'O'






# This assignment is about File input/output (or File I/O).
# Like for most other tasks, Python provides a lot of flexibility when it comes to
# reading from and writing to files.

# Let's directly jump to examples.

# Let us start by creating a file and then reading it using a Python code.
# Use your favourite text editor and write something into a file and save it.
# I am naming the file 'simple_text.txt'. I am going to write the following content.
#
# This is line 1.
# This is line 2.
# This is the last line.
#

# To open this file, you need to use the in-built function 'open()' as follows.

###f = open('simple_text.txt','r')

# The first argument to the 'open()' function is the name of the file, it should be given as string.
# You can give a path to the file also, example- '/home/sampada/some_directory/simple_text.txt'.
# If you give only the file name, then it means that the file is kept in the same folder as
# that of the code.

# The second argument specifies the mode in which you want to open the file. In the above example,
# we have used 'r' as the mode which stands for the 'read mode'.

# This 'open()' function returns a 'file object' or a 'file handle' which we have stored as the variable
# 'f' in the above example. There are several methods available for 'file handle', like reading, writing.
# Let us use some of these methods in the following sections.

#############################################################################################


# close() method:
# This is perhaps the most important method of a file object. It is a good practice to close an opened 
# file after you are done with your work.

###f.close()

#############################################################################################


# read() method:
# It reads some quantity of data from file. It takes an optional integer argument which specifies how many
# bytes to read. Note that one letter/character corresponds to one byte. So you can easily spefify how many
# characters to read.
"""
f = open('simple_text.txt','r')
print(f.read())
f.close()
print("\n")

f = open('simple_text.txt','r')
print(f.read(6)) # Get first 6 characters from file
f.close()
print("\n")
"""
#############################################################################################


# readline() method:
# This method reads the file line by line. Every time you call this method, it returns one line until
# all the lines in the file are over.
"""
f = open('simple_text.txt','r')
print(f.readline()) # First line
print(f.readline()) # Second line
print(f.readline()) # Third line
print(f.readline()) # All lines are over. This doesn't return anything
f.close()
print("\n")
"""

# An easier way to print all lines in a file-
"""
f = open('simple_text.txt','r')
for line in f:
	print(line)
f.close()
"""
# Notice that we have not even called the readline() function. The file object works as an iterable object.
# This way, the Python interpreter can read large files very efficiently.

#############################################################################################


# Closing the file without explicitly calling the 'close()' method:
# The following syntax creates the file object f and closes the file as soon as the program is out of
# the 'with' block. This way, you do not have to worry about closing the files.
"""
with f as open('simple_text.txt','r'):
	for line in f:
		print(line)
"""
#############################################################################################


# Writing to a file:
# You need to open the file in write mode, 'w'.
"""
f = open('myfile.txt','w')
f.write("Guten Morgen! Gestern war der Bundestag in Deutschland.\n",
f.close()
"""
# Now open the file in a text editor and confirm that the writing was successful.

#############################################################################################


# Appending to existing content of a file:
# You have to use the append mode, 'a'.
# Let's try to append a line to the file we wrote in the previous example.
"""
f = open('myfile.txt','a')
f.write("Wir haben viel Spass gemacht!!\n")
f.close()
"""
# Open the file in a text editor and confirm.

#############################################################################################


# There are many other mehods of the file object. But these are the ones that you will use most commonly.

# You can find many more methods here- https://docs.python.org/3/tutorial/inputoutput.html
# Go to section- '7.2. Reading and Writing Files'

#############################################################################################




# Question 1:
# Copy content of one file into another, line by line. Do not use Linux's copy command :P :)

# Solution 1:
# I am going to leave this for you to do. It is not very difficult.
# All you have to do is keep two files open, one in read mode and one in write mode.
# Then in a loop, read lines from one file and in every iteration of the loop write that that line into another file.
# Finally, outside the loop you have to close both the files.

#############################################################################################


# Question 2:
# Following is the data you need to write to a file. Can you write it in a comma separated format?
# Here's how the content of the file should look.
#
# Sr.No.,Name,CGPA,DegreeAwarded
# 1,Sampada,7.3,True
# 2,Supriya,7.8,True
#
# Same for other lines.

# Solution 2:
# I have made only small changes to your code.
# The 'linei' variable which you have creaed can be created directly as a string variable.
# I have concatanated all the required values using a comma in between.
# Once it is a string, the write() function of file can directly take it as an argument.
# I have used f.write(linei + "\n"), so 'linei + "\n"' is actually the argument to the write() function.

data = {1: {'Name':'Sampada', 'CGPA':7.3, 'DegreeAwarded':True},
				2: {'Name':'Supriya', 'CGPA':7.8, 'DegreeAwarded':True},
				3: {'Name':'Anuja',   'CGPA':7.9, 'DegreeAwarded':True},
				4: {'Name':'Sumedha', 'CGPA':7.1, 'DegreeAwarded':True}}

f = open('studentdatafile.txt','w')

f.write('Sr. No.,Name,CGPA,DegreeAwarded\n')
for i in data.keys():
	linei= str(i) + "," +  data[i]['Name'] + "," + str(data[i]['CGPA']) + "," + str(data[i]['DegreeAwarded'])

	# Or, if you really want to make it look more fancy, then do the following :)
	# It takes the requred values as a list and joins them by comma. Read more about join() method for strings.
	#linei= ','.join([str(i), data[i]['Name'], str(data[i]['CGPA']), str(data[i]['DegreeAwarded'])])

	#print(linei)
	#print(type(linei))
	f.write(linei + "\n")

f.close()

print("\n#########################\n")

#############################################################################################

# Question 3:
# I have given a file 'molecule.csv'. You can open it in gedit or any other text editor to check it's content.
# The file has 4 columns- Atom,X,Y,Z. Atom is the name of an atom. X, Y, Z are the coordinates.
# For general understanding of what the molecules looks like, check out the image of the molecule- molecule.png.
# Do the following-
# Print the contents of the file in a tabular format on command-line.
# Calculate the centroid coordinates of the molecule.
# Calculate the centroid of the ring formed by carbon atoms- CG, CD1, CD2, CE1, CE2, CZ.
# Calculate average carbon-carbon bond length. Note: All atoms whose names are starting with 'C' are carbons.
# Calculate all-to-all euclidean distance matrix for this molecule and write it to another file.

# Solution 3:
# 

# Read the file and create list of lists, for example-
# mol = [ [AtomName1,X1,Y1,Z1], [AtimName2,X2,Y2,Z2], [AtomName3,X3,Y3,Z3] ]
f = open("molecule.csv",'r')

# Iniialize empty list to which we will append the sub-lists for atoms.
# I have given the name 'mol' as a short for molecule :)
mol = []

# Read the first line, but we do not have to store it right now. It is just the header.
# Note that after reading each line, the Python interpreter is waiting at the end of that line.
# So when you try to read more lines, it directly starts from there. It will not read this line again.
f.readline()

# This is now reading from the second line in the file, because we have already read one line in the previous step.
for line in f:
	# Strip trailing empty spaces or newline characters from both sides of the string.
	line = line.strip()

	# Continue with next iteration of loop without doing any further steps if line is empty.
	if line == "":
		continue

	# Split line by comma. This returns you a list of all the values in the line.
	row = line.split(",")
	#print(row)

	# X, Y and Z are numbers, so we convert the corresponding elements in the list to float.
	row[1] = float(row[1])
	row[2] = float(row[2])
	row[3] = float(row[3])

	# Append this list 'row' (which represents information of one atom here) to the list we created before.
	mol.append(row)

f.close()

# The list 'mol' now contains many small lists (of length 4 each). Each sub-list represents one atom.

################################################################################

# Print the contents of the file in a tabular format on command-line.
print("Contents of the file in tabular format:")
# This loop iterates over the list 'mol' which is a list of lists.
for atom in mol:
	# Print values of list with tab (or '\t') as separator.
	print(atom[0] + "\t" + str(atom[1]) + "\t" + str(atom[2]) + "\t" + str(atom[3]))

	# Fancy way to do the same thing :)
	#print("\t".join([str(val) for val in atom]))
print("\n")
print("\n#########################\n")

################################################################################

# Define a generalized function for centroid calculation
def centroid(points):
	# This function takes a list of lists as a parameter, named 'points' here.
	# So 'points' should have following structure.
	# points = [ [x1,y1,z1], [x2,y2,z2], [x3,y3,z3], [x4,y4,z4],... ]
	# Length of 'points' could ee anything. But each sublist should have length 3, i.e. only 3 coordinates- x, y, z.

	# Initialize centroid coordinates to zero.
	cen = [0.0,0.0,0.0]

	for point in points:
		i = 0
		for coord in point:
			# Add all corresponding coordinates, i.e. x1+x2+x3..., y1+y2+y3... etc.
			# The variable 'i' takes values 0, 1, 2 repeatedly, so that we can sum up the corresponding coordinates.
			cen[i] += coord
			i += 1

	if len(points) > 0:
		i = 0
		# Now divide each summed up coordinate value by length of 'points', which is the number points for which we are calculating the centroid.
		for x in cen:
#			print cen[i]
			cen[i] /= len(points)
			i += 1

	# Return the centroid as a list of length 3
	return(cen)
###END FUNCTION centroid()###

################################################################################

# To use the above centroid function, we need a list of points which contains only the coordinates, not the atom names.
# So first make that list of lists.
coordinates = []
for atom in mol:
	# atom[1:] will give you sublist with all elements starting at index 1. Refer to list comprehensions.
	coordinates.append(atom[1:])

print("Centroid:",centroid(coordinates))
print("\n#########################\n")

################################################################################

# To get coordinates of all ring atoms, we can iterate over the list 'mol' and take only those atoms whose names are found in the given set of names.
coordinates = []
for atom in mol:
	if atom[0] in ['CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ']:
		coordinates.append(atom[1:])

print("Centroid of ring:",centroid(coordinates))
print("\n#########################\n")

################################################################################

# For the third question, you might realize that it will be complicated to get data for speficif atoms from the 2D list 'mol'.
# A better way would be to make it a dictionary, with keys as atom names and values as [X,Y,Z] coordinates.
# This will be then a dictionary of lists.
# Let's read the file again and do that.

f = open("molecule.csv",'r')

# This is the dictionary we want to fill.
coord = {}

# Read header line.
header = f.readline()
print("This was header, but we don't need it right now. - " + header)

for line in f:
	line = line.strip()

	if line == "":
		continue

	row = line.split(",")
	#print(row)

	row[1] = float(row[1])
	row[2] = float(row[2])
	row[3] = float(row[3])

	# Everything in this loop upto here is done same as before.
	# But we store the data as a dictionary now, with atom name i.e. row[0] as the key.
	# The remaining elements of the list 'row' are stored as value, which is infact a list.
	# This is how it becomes a dictionary of list. It will look something like this-
	# coord = {'AtomName1':[x1,y1,z1], 'AtomName2':[x2,y2,z2], ...}
	coord[row[0]] = row[1:]

f.close()

# Try printing this dictionary to see how it actually looks.
# print(coord)


################################################################################

# Print and check that we have stored the data the way we wanted
print("Contents of the molecule:")
for atom in coord:
	print(atom,"--->",coord[atom])
print("\n")

print("\n#########################\n")

################################################################################

# We need this module to find square root.
# I do not remember how to find square root numerically :P :) That could be a big procedure!
import math

def dist(p1,p2):
	# This function finds euclidean distance between two points.
	# The function takes two lists (of same length) as parameters.
	s = 0
	if len(p1) == len(p2):
		i = 0
		while i < len(p1):
			s += (p1[i]-p2[i])**2
			i += 1

	return(math.sqrt(s))
###END FUNCTION dist(p1,p2)###

################################################################################

# I am hard-coding the distance calculation here, because there was no information about bonded atoms inside the file.
d = 0
d += dist(coord['CA'],coord['C'])
d += dist(coord['CA'],coord['CB'])
d += dist(coord['CB'],coord['CG'])
d += dist(coord['CG'],coord['CD1'])
d += dist(coord['CG'],coord['CD2'])
d += dist(coord['CD1'],coord['CE1'])
d += dist(coord['CD2'],coord['CE2'])
d += dist(coord['CE1'],coord['CZ'])
d += dist(coord['CE2'],coord['CZ'])

print("Average carbon carbon bond length:",d/9,"\n")

print("\n#########################\n")

################################################################################

# To calculate the distance matrix (all-to-all atoms), we need two 'for' loops.
# Important thing is to remember that our data structure 'coord' is a dictionary. So it has unordered keys.
# So every time you do coord.keys(), you might get the keys in different order!
# And this could create confusion. Easiest way to be sure about the ordering is to get the keys and sort them.
# Of course, this sorting be very time consuming if there are too many keys (may be more than 100000). But for this example, it is fine.
print("All to all atom euclidean distance matrix:\n")
print("\t"+"\t".join([atom for atom in sorted(coord.keys())]))
for atom1 in sorted(coord.keys()):
	print(atom1,end="\t")
	for atom2 in sorted(coord.keys()):
		print('{:.3f}'.format(dist(coord[atom1],coord[atom2])),end="\t")
	print()

################################################################################




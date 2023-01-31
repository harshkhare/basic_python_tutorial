
# Let us revise the fundamentals by doing some text analysis and information theory.
# Of course, it will not cover everything but it should get you going.

# Consider these questions.
# Question 1: How likely is your name among Indian female names?
# Question 2: How much information is there in the names? (Assuming that all letters are considered independently)
# Question 3: Is there more information in the first letters of the names than in the other positions?


##########################################################################

# The most important thing to note is that this is natural text data,
# i.e. there are going to be anomalies, special cases, errors etc.
# Always remember to think about preprocessing data before doing any maths with it.
# And it is more critical with text data as problems in text data are not always intuitive.
# Here, there won't be many problems (except for duplication) because it is only a list of names.
# But we need to make some assumptions about these data to keep our calculations simple.
# Assumption 1: Our list of names is exhaustive. (See attached list of Indian female names).
# Assumption 2: Each spelling represents unique name. It will be very complex if we want to associate spelling variations to a single name.


##########################################################################

# Let's come back to the questions.

# Question 1:
# How likely is your name among Indian female names?
# 
# You can calculate the probability of a name in several different ways.
# 
# Simple way, without considering order of letters-
# P(name) = PROD[P(letter)]   for all letters in name.
#
# Slightly better way, considering position of letter in the name
# P(name) = PROD[P(letter_at_position)]   for all letters in name.
#
# Even better way, using conditional probabilities, i.e. Markov chains
# P(name) = PROD[P(letter|previous_letter)]   for all letters in name.


# For the purpose of revision, it might be enough to implement the simple way.
# But you can think of more elaborate ways if time permits.
#
# Here are possible steps to implement the simple way (i.e. without considering the order of letters in names).
#
# 1. Read file containing names, one on each line.
# 2. Store the names as a list of strings. Remember to make all lower case or upper case.
# 3. Declare a dictionary to store counts of alphabets. Keys as alphabets (a to z) and initial values as zeros.
# 4. Similarly, declare a dictionary to store probabilities of alphabets.
# 5. For each word, count the occurrence of each letter and add it to the count.
#    Something like this-
#
#    count_dictionary = {'a':0, 'b':0, 'c':0, ...}
#    for letter in count_dictionary:
#   		for name in names:
#     		count_dictionary[letter] += name.count(letter)
#
# Once the counts are ready, run a for loop on the dictionary and divide each value by the sum of all values to get probabilities.
#
# To calculate probability of a given name, just multiply the probabilities associated with it's letters.
# You can write a function to do this, which takes a name and returns the probability.


##########################################################################

# The second and the third question talk specifically about quantitative measure of information content.
#
# The concept of the Shannon's entropy or Information entropy will be useful here.
#
# You may like to read about intuition behind Shannon's entropy.
# https://towardsdatascience.com/the-intuition-behind-shannons-entropy-e74820fe9800


##########################################################################

# Question 2:
# How much information is there in the names? (Assuming that all letters are considered independently)
#
# Here, we will not consider the position of letters or combinations of letters.
# Consider all the names in our list as a pool of letters. We can easily calculate the information entropy of this pool
# by using the formula for Shannon's entropy.
#
# H = -SUM[ P(letter)*log(P(letter) ]
#
# Try to implement this.


##########################################################################

# Question 3:
# Is there more information in the first letters of the names than in the other positions?
#
# Like we calculated the Shannon's entropy for the whole set of letters, we can also calculate it for each position.
# If all letters are eqally likely in a given position then there is maximum information entropy at that position.
# Or you can say there is a lot of information at that position.
# If only one letter dominates a position, then that position does not contain much information and has very low information entropy.
#
# s a m p a d a
# a n u j a
# s u m e d h a
# r e s h m a
# n a m r a t a
# i s h i t a
# v i s h a l
# h a r s h
# s u p r i y a
# s o n a l i
# s i d d h a r t h
# v i n a y
#--------------------
# 1 2 3 4 5 6 7 8 9  <--------- Positions
#
# Consider the letters at each position as one set and calculate probability of each letter in that set.
# If you make a dictionary to store this, it might look something like this-
# d = { 1 : {'a':345, 'b':137, 'c':98,  'd':238 ...},
#     { 2 : {'a':872, 'b':437, 'c':221, 'd':342 ...}, ...}
#
# where the keys 1, 2 etc. indicate the position.
# The values are dictionaries, each holding counts or probabilities for 26 letters at that particular position.
#
# Now for each position, you will have to separately calculate the Shannon's entropy.
# Then you can tell, which position is the has how much information content.
#
# One thing to note: You will have to find out the maximum length of the names first,
# so that you can decide how many positions to consider for calculation of position specific Shannon's entropy.


##########################################################################

# Additional comments
#
# My understanding of information content-
# This is just to give my perspective. Tell me if you think of any more examples to explain this concept to others.
# 
# If I say the name starts with 'A', then there are too many such names.
# A fact that the name starts with 'A' is not highly informative.
# But if I say that the name starts from 'U', then there are only a few possibilities.
# This statement gives me a lot of information. It reduces my search space.
# The definition of information content appropriately describes this behavior.
# Information content = log(1/P(x))
# In other words, the most unlikely events are the most informative (or have hither entropy).

##########################################################################




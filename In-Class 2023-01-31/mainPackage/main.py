#main.py
# create an empty list
myList = []
'''
print(type(myList))
# append 42 to the list
myList.append(42)
# how many elements are now in the list?
print(len(myList))
# add 5 random ints to the list
import random
for i in range(0,5): # number of random integers to import
    myList.append(random.randint(0,42))
print(myList) # on print we know its a list based on [] it is in

# indexing. square brackets again

# the second element in myList
print(myList[1]) # square brackets are pronounced as sub, so it would be print myList sub 1....we index from 0
# fancy indexing print last element in list assume you don't know how long the list is
print(myList[-1]) # always the last element
# the second and third elements using slicing
print("Second and third elements:", myList[1:3]) # leave out the step if it is one, that is the default

print(myList[-3:-1]) # will not include the last element
'''
# make a tuple with 5 numbers from 5 to 9
myTuple = (5,6,7,8,9)
print(type(myTuple))
# change the 7 to a 99
# myTuple[2] = 99 this does not work, will crash
# convert the tuple to a list
myNewList = list(myTuple)
print(type(myNewList), myNewList)
# create a 2 by 3, 2 rows, 3 columns data structure 
# use list of lists, initialize 1,2,3,4...
myMatrix = [   # can put it all in one row, but easier to visualize in mulitple rows
    [1,2,3],
    [4,5,6]]
print(myMatrix)
# what is len of myMatrix?  it looks at the number elements, aka rows
# change 5 to 99
myMatrix[1][1] = 99 # first one is the row, second is column
for row in myMatrix: # to print like a table or matrix would look like
    print(row)
# model a student at UC
# in a list store:
# mNumber
# gpa
# one element with high school graduation year and expected UC graduation year
# major
me = [5482895,
      3.89,
      (2005, 2023),
      "Accounting and IS"] # this can be done multiple ways
print(me)
me2 = ["M05482895",    # heterogeneous list ie different types of elements
       3.89,
       [2005, 2023],
       "Accounting and IS"]
print(me2)
for i in me:
    print(type(i)) # prints individual type for each element
for i in me2:
    print(type(i))
    
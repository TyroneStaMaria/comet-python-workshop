names = ["Gavin", "Vince", "Riley", "Mark"]

# indeces can also be negative 
print(names[-1]) # this will print out the last item of the list
print(names[-2]) # this will print out the 2nd to the last item of the list

# you can also get how many items are inside a list by using the len() function
print('Length - ',len(names))


# append - add an item at the end of the list
names.append("Kendrick")
print("Append - ", names)

# pop - removes an item at the end of the list
names.pop()
print("Pop - ",names)

# index - get the index of the first element with the specified value
vince_index = names.index("Vince")
print("Index - ", vince_index)
# print(names.index("Tyrone")) # the program will throw an error when you try to put in a value that is not part of the list 

# sort - sorts the list
names.sort()
print("Sort - ", names)


names = ["Gavin", "Vince", "Riley", "Mark"]

""" 
slicing - select items in a list within a certain range names[start:stop:step]

The start index specifies the index that the slicing starts from. The default is 0.
The end index specifies the index where the slicing ends (but excluding the value at this index). The default is the length of the array.
The step argument specifies the step of the slicing. The default is 1.

Learn more at: https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/
"""

print("Slicing - ", names[1:3]) 

# leave the stop blank if you want it until the last item
print("Slicing - ", names[1:])

# you can also leave the start  blank if you want to include the first item
print("Slicing - ", names[:2])


names_2 = ["Wilfred", "Jihro", "Greco", "Eric"]

# you can combine lists together by adding them using the '+' operator
new_names = names + names_2
print(new_names) 
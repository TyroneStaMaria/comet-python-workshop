
"""
  Bonus 1:
  The in keyword 
  
  This keyword is used to check if a value is in a sequence (list, tuple, string, etc.)
"""
# Check if a value is in a list
names = ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]
print("Briane" in names) # True
print("Briane" not in names) # False

# The keyword can also be used to check if a value is in a string
name = "Briane"
print("B" in name) # True
print("B" not in name) # False

# The keyword is also used to iterate through a sequence in a for loop
for name in names:
  print(name)



"""
  Bonus 2:
  List comprehension - this is a shorter way of creating a new list from an existing list
"""
names = ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]
names_with_a = []

# This is how we can do this with a for loop
for name in names:
  if "a" in name:
    names_with_a.append(name)

print(names)

# This is how we can do this using list comprehension
names_with_a = [name for name in names if "a" in name]



"""
  Bonus 3:
  Assignment unpacking - this is a way to assign values to multiple variables at once
"""
# This is how we can do this without assignment unpacking
names = ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]
name1 = names[0]
name2 = names[1]
name3 = names[2]
name4 = names[3]
name5 = names[4]
name6 = names[5]

# This is how we can do this with assignment unpacking
name1, name2, name3, name4, name5, name6 = names

# We can also use assignment unpacking to swap the values of two variables
a = 1
b = 2
a, b = b, a

print(a) # 2
print(b) # 1


"""
  Bonus 4:
  The enumerate function - this is a function that returns an enumerate object which contains the index and value of each item in a sequence
"""
names = ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]

# This is how we can do this without the enumerate function
for index in range(len(names)):
  print(index, names[index])

# This is how we can do this with the enumerate function
for index, name in enumerate(names):
  print(index, name)


"""
  Bonus 5:
  String functions - these are functions that can be used to manipulate strings
"""

# The upper function - this function returns a string with all the characters in uppercase
name = "Briane"
print(name.upper()) # BRIANE

# The lower function - this function returns a string with all the characters in lowercase
name = "Briane"
print(name.lower()) # briane

# The split function - this function returns a list of strings that were separated by a delimiter
name = "Briane Unisse Austin Jordan Miko Tyrone"
print(name.split(" ")) # ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]

# The join function - this function returns a string that was joined by a delimiter
names = ["Briane", "Unisse", "Austin", "Jordan", "Miko", "Tyrone"]
print(", ".join(names)) # Briane, Unisse, Austin, Jordan, Miko, Tyrone

# The replace function - this function returns a string with all the occurrences of a substring replaced with another substring
name = "Briane"
print(name.replace("B", "b")) # briane

# The strip function - this function returns a string with all the leading and trailing whitespaces removed
name = " Briane  "
print(name.strip()) # Briane

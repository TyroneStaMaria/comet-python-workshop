user = {
  "name": "Tyrone",
  "age": 22
}

# you can access an item in a dictionary by referring to its key
print(user["name"])

# you can modify the value of an item by reassigning it
user["name"] = "Gavin"
print(user["name"])

# you can add items to the dictionary by using a new index key and assigning a value to it
user["email"] = "gavindizon@gmail.com" 

# items - the items() method returns each items in a dictionary as tuples in a list
# [(name, Tyrone), (age, 22)]
print(user.items())

# keys - the keys() method returns keys in a dictionary in a list
# ["name", "age"]
print(user.keys())

# values - the values() method returns values in a dictionary in a list
# ["Tyrone", 22]
print(user.values())

# update - the update() method  will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# There is no difference when you use this over the value assignment. However, this is more useful when you want to add/modify multiple values in a dictionary
user.update({"gender": "male", "age": 23, "course": "Computer Science"})
print(user)
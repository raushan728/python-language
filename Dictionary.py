#1. Creating a Dictionary

# Empty dictionary
dict1 = {}

# Dictionary with values
student = {
    "name": "Raushan Singh",
    "age": 19,
    "course": "AI & ML"
}

#2. Accessing Values

#🔹 Difference Between [] and .get():
#student["marks"] → Error if key doesn’t exist.
#student.get("marks", "Not Found") → Returns default value if key doesn’t exist.
print(student["name"])  # Output: Raushan Singh
print(student.get("age"))  # Output: 19

#3. Adding a New Key-Value Pair

student["city"] = "Delhi"
print(student)  
# Output: {'name': 'Raushan Singh', 'age': 19, 'course': 'AI & ML', 'city': 'Delhi'}

#4. Updating an Existing Key

student["age"] = 23
print(student["age"])  # Output: 23
#Another way using update()
student.update({"age": 24, "country": "India"})
print(student)
# Output: {'name': 'Raushan Singh', 'age': 24, 'course': 'AI & ML', 'city': 'Delhi', 'country': 'India'}

#5. Removing Items from Dictionary

# Using del
del student["city"]
print(student)  # 'city' removed

# Using pop() - Returns removed value
age = student.pop("age")
print(age)  # Output: 24
print(student)  # 'age' removed
#Explanation:
#"age": 22 is removed.
#The value 22 is returned and stored in the variable age.

# Using popitem() - Removes last inserted item (Python 3.7+)
student.popitem()
print(student)  # Last item removed

# Using clear() - Removes all elements
student.clear()
print(student)  # Output: {}

#6. Checking if a Key Exists

if "name" in student:
    print("Key exists")

print("city" in student)  # Output: False

#7. Iterating Over Dictionary

student = {"name": "Raushan", "age": 22, "course": "AI & ML"}

# Looping through keys
for key in student:
    print(key)  # Prints keys

# Looping through values
for value in student.values():
    print(value)  # Prints values

# Looping through both keys and values
for key, value in student.items():
    print(key, ":", value) #prints key and values 

#8. Copying a Dictionary

student_copy = student.copy()
print(student_copy)

#9. Getting Dictionary Keys and Values

keys = student.keys()
values = student.values()
items = student.items()

print(keys)    # dict_keys(['name', 'age', 'course'])
print(values)  # dict_values(['Raushan', 22, 'AI & ML'])
print(items)   # dict_items([('name', 'Raushan'), ('age', 22), ('course', 'AI & ML')])

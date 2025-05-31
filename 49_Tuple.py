#1.Creating a Tuple

my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple) # Output Tuple: (10, 20, 30, 40, 50)

#2.Accessing Elements (Indexing & Slicing)

print(my_tuple[1])     # Output: 20
print(my_tuple[-1])    # Output: 50
print(my_tuple[1:4])   # Output: (20, 30, 40)

#3. Tuples are Immutable

my_tuple[2] = 99  # Error (TypeError: 'tuple' object does not support item assignment)

#4.Tuple Concatenation & Repetition

new_tuple = my_tuple + (60, 70)
print("Concatenated Tuple:", new_tuple) #Output Concatenated Tuple: (10, 20, 30, 40, 50, 60, 70)
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple) # Repeated Tuple: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# 5.Checking Element in Tuple (in Operator)

print(50 in my_tuple)  # Output: True
print(100 in my_tuple) # Output: False

#6.Tuple Packing & Unpacking

# Packing
person = ("Raushan", 22, "AI Engineer")

# Unpacking
name, age, profession = person
print("Name:", name) #Output Name: Raushan
print("Age:", age) #Output Age: 22
print("Profession:", profession) #Output Profession: AI Engineer

#7.Finding Length & Count

print(len(my_tuple))     # Output: 5
print(my_tuple.count(30)) # Output: 1
print(my_tuple.index(40)) # Output: 3
#1. Creating a Set

# Empty set (use set() instead of {})
set1 = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

#2. Adding Elements to a Set

numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

#3. Removing Elements from a Set

# remove() - Gives error if element not found
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}

# discard() - No error if element not found
numbers.discard(10)  # No error even if 10 is not in set

# pop() - Removes and returns a random element
element = numbers.pop()
print(element)  # Random element removed
print(numbers)

# clear() - Removes all elements
numbers.clear()
print(numbers)  # Output: set()

#4. Checking Membership in a Set

numbers = {1, 2, 3, 4, 5}
print(2 in numbers)  # Output: True
print(10 in numbers)  # Output: False

#5. Set Operations (Union, Intersection, Difference, Symmetric Difference)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union -> {1, 2, 3, 4, 5, 6}
#print(A.union(B))
print(A & B)  # Intersection -> {3, 4}
#print(A.intersection(B))
print(A - B)  # Difference -> {1, 2}
#print(A.difference(B))
print(A ^ B)  # Symmetric Difference -> {1, 2, 5, 6}
#print(A.symmetric_difference(B))

#6. Copying a Set

B_copy = B.copy()
print(B_copy)  # Output: {3, 4, 5, 6}
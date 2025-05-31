#1.Creating a List

my_list = [10, 20, 30, 40, 50]
print("List:", my_list)  #output List: [10, 20, 30, 40, 50]

#2. Accessing Elements (Indexing & Slicing)

print(my_list[1])     # Output: 20 (Indexing)
print(my_list[-1])    # Output: 50 (Negative Indexing)
print(my_list[1:4])   # Output: [20, 30, 40] (Slicing)

#3.Updating Elements

my_list[2] = 99
print("Updated List:", my_list) #Output Updated List: [10, 20, 99, 40, 50]


#4. Adding Elements (append(), insert(), extend()

my_list.append(60)   # Add at end
my_list.insert(2, 15) # Insert at index 2
extra = [70, 80]
my_list.extend(extra) # Add multiple elements

print("List after adding elements:", my_list) #Output List after adding elements: [10, 20, 15, 99, 40, 50, 60, 70, 80]

#5. Removing Elements (remove(), pop(), del

my_list.remove(99)   # Remove specific element
my_list.pop(3)       # Remove element at index 3
del my_list[0]       # Delete first element
#del my_list[1:3]  # Elements at index 1 and 2 will be deleted
#print(my_list)  # Output: [10, 40, 50]
print("List after deletions:", my_list) #Output List after deletions: [20, 15, 40, 50, 60, 70, 80]

#6.Checking Element in List (in Operator)

print(50 in my_list)  # Output: True
print(100 in my_list) # Output: False

#7.Sorting & Reversing

my_list.sort()      # Sorts in ascending order
#my_list.sort(reverse=False) Same output
#my_list.sort(reverse=True) # In Descending order
my_list.reverse()   # Reverses the list
print("Sorted and Reversed List:", my_list) #Output Sorted and Reversed List: [80, 70, 60, 50, 40, 20, 15]
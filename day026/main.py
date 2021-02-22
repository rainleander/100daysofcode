# List Comprehension
# Create a new list from a previous list
# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)
# output: [2, 3, 4]

# challenge: what will happen when list comprehension is applied to a string?
name = "Rain"
name_list = [letter for letter in name.lower()]
print(name_list)
# output: ['r', 'a', 'i', 'n']

# challenge: create a new list from a range, where the list items are double the values in a range
single_range = range(1,5)
double_range = [x*2 for x in single_range]
print(double_range)
# output: [2, 4, 6, 8]

# Things I have learned

# Reverse a string
my_string = 'Hello world!'
print(my_string[::-1])

# Join strings
print(' '.join('PYTHON PROGRAMMING'))

# Print formatting
print(f'This is a message: {my_string}')

# Make repetitive lists
my_list = [1, 2, 3] * 2
print(my_list)

# Make list from range
my_list2 = list(range(5, 7)) * 3
print(my_list2)

# Zip the lists together (think zipper on a jacket)
print(list(zip(my_list, my_list2)))

# Pop the last element from list
print(my_list.pop())

# List comprehensions with if and if + else
print([x for x in range(1, 11) if x % 2 == 0])
print([x if x % 2 == 0 else 'ODD' for x in range(1, 11)])

# List comprehensions with nested for loops
print([x * y for x in [1, 2, 3] for y in [1, 10, 100]])

# List comprehensions with list of lists
print([[x ** 2 for x in y] for y in [[1] * 3, [2] * 3, [3] * 3]])

# Random int and shuffle (list)
from random import randint, shuffle
print(f'A random integer is: {randint(2, 8)}')
shuffle(my_list)
print(f'Shuffling my_list: {my_list}')

# Possible to use else in while or for loops
x = 0
while x <= 2:
    print(x)
    x += 1
else:
    print('Done!')

for num in my_list2[0:2]:
    print(num)
else:
    print('Done again!')

# Files
with open('text.txt', 'r') as file:
    # Print each line of the file
    print(file.read())
    # Put the cursor to the BOF
    file.seek(0)
    # Print each line -> list
    print(file.read().split('\n'))
    # Print each line -> list
    file.seek(0)
    print(file.readlines())

help(my_list.insert)

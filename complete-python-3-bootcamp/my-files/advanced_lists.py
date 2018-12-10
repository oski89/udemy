l = [1, 2, 3, 3, 4]
l.append([5, 6])  # appends the list as an item
print(l)

l = [1, 4, 3, 3, 2]
l.extend([5, 6])  # extends the list
print(l)

print(l.index(3))  # returns the index of the first occurance of the item

l.insert(2, 'inserted')  # insertes at index
print(l)

l.remove(3)  # removes the first occurance
print(l)

l.remove('inserted')
l.sort()  # removes the first occurance
print(l)

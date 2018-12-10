# advanced sets

s = set()

s.add(1)
s.add(2)
print(s)
s.add(2)  # won't add 2 since it is already in set
print(s)

sc = s.copy()  # makes a copy of set s
s.add(4)  # adds 4 to set s
print(s)

print(s.difference(sc))  # prints elements in s1 not found in s2

s1 = {1, 2, 3}
s2 = {1, 4, 5}
print("s1:", s1)
print("s2:", s2)

s1.difference_update(s2)
print(s1)

s.discard(2)
print(s)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))  # prints elements in s1 found in s2

s1.intersection_update(s2)
print(s1)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s2))  # returns True if s1 and s2 don't have elements in common
print(s1.isdisjoint(s3))

print(s1.issubset(s2))  # returns True if s1 is a subset of s2
print(s2.issuperset(s1))  # returns True if s2 is a superset of s1
print(s1.symmetric_difference(s2))  # returns elements that differ by symmetry
print(s1.union(s2, s3))  # joins all sets


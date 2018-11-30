'''
Collections modules covered:
* Counter
* defaultdict
* OrderedDict
* namedtuple
'''

from collections import Counter, defaultdict, OrderedDict, namedtuple

'''
START OF COUNTER
'''

# Count the values in a list and return a dict with results
llist = [32,2,5,6,7,7,7,5,3,3,5,8,9,9,0,9,7,5,34,3,2,2,3,6,78,9,98,7654,2,23,456,78,9,876]
print(Counter(llist))

# Count the values in a string and return a dict with results
Counter('asuvbsweiofahskdfhsek7lifhudcvskduxrguhfdoisuzkegfdhbvoisuekdgxdfhoiwjksughxfbva')

# Count the words in a string splitted into a list and return a dict with results
s = 'How many times will this word end up word in how many will end this will times'
words = s.split()
print(Counter(words))

# Show the 4 most common words
c = Counter(words)
c.most_common(4)

# total of all counts
print(sum(c.values()))

# reset all counts
print(c.clear())

# list unique elements
print(list(c))

# covert to a set
print(set(c))

# convert to a regular dictionary
print(dict(c))

# convert to a list of (elem, cnt) pairs
print(c.items())

# convert from a list of (elem, cnt) pairs
print(Counter(dict(c.items())))

# 3 least common elements
c.most_common()[:-3-1:-1]

# remove zero and negative counts
c += Counter()

'''
END OF COUNTER
'''

'''
START OF DEAFULTDICT
'''

# Create a dict with default values that never give errors
d = defaultdict(object)
d['one']
for item in d:
    print(item)

# Create a dict with default values that never give errors
d = defaultdict(lambda: 0)
d['hej']

'''
END OF DEFAULTDICT
'''

'''
START OF ORDEREDDICT
'''

# Normal dictionary
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

# Ordered dictionary
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

'''
END OF ORDEREDDICT
'''

'''
START OF NAMEDTUPLE
'''

Dog = namedtuple('Dog', 'name age breed color')
elsa = Dog(name='Elsa', age=8, breed='Westie', color='white')
nisse = Dog(age=5, color='black', name='Nisse', breed='Husky')

print(elsa)
print(elsa.name)
print(nisse[0])
print(nisse.breed)

'''
END OF NAMEDTUPLE
'''

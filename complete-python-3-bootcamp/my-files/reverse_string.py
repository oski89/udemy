# Reverse a string
string = 'abcdefghijk'
print(string)

# The python way
my_string = string[::-1]
print(my_string)

# The for loop way
my_string = ''
for i in range(len(string) - 1, -1, -1):
    my_string += string[i]
print(my_string)

# String formatting and f-strings
# Float formatting follows "{value:width.precision f}"

print('The {q} {b} {f}.'.format(f='fox', b='brown', q='quick'))

result = 194.12345
print('The result was {r:1.2f}.'.format(r=result))

name = 'Jose'
print(f'Hello, his name is {name}.')

hour = 6
minutes = 32
print(f'I woke up at {hour:02}:{minutes}.')

print('I once caught a fish %s.' % 'this \tbig')
print('I once caught a fish %r.' % 'this \tbig')

s = 'Hello world!'

# Capitalize
print(s.capitalize())

# Upper
print(s.upper())

# Lower
print(s.lower())

# Count
print(s.count('o'))

# Find
print(s.find('l'))

# Formatting
# Center
print(s.center(20, '-'))

# Tab (alt 1 or 2)
print('hello\tworld')
print('hello\tworld'.expandtabs())

# Check cases
print('python3'.isalnum())  # is alphanumerical? --> True / False
print('python'.isalpha())  # is alphabetical? --> True / False
print('python'.islower())  # is lowercase? --> True / False
print('PYTHON'.isupper())  # is uppercase? --> True / False
print('    '.isspace())  # is space? --> True / False
print('Python Rocks'.startswith('Py'))  # starts with text? --> True / False
print('Python'.endswith('on'))  # ends with text? --> True / False

# Split (splits at every instance and excludes split character)
print('Hello World!'.split('o'))

# Partition (splits at first instance and includes split character)
print('Hello World!'.partition('o'))

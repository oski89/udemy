import re

# MATCH WITH REGEX

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print(f'Searching for "{pattern}" in:\n "{text}"\n')

    # Check for match
    match = re.search(pattern, text)
    if match:
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

# New pattern
pattern = 'term1'

# Match pattern in text
match = re.search(pattern, text)
print(type(match))

# Show start of match
print(match.start())

# Show end of match
print(match.end())

# SPLIT WITH REGEX

# Term to split on
split_term = '@'

# Phrase to parse
phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the parse
print(re.split(split_term, phrase))

# Phrase 2 to parse
phrase2 = 'Now, we will split on comma, which is good, since the comma can be used a lot, and I mean a lot.'

# Split the parse
print(re.split(',', phrase2))

# FINDALL WITH REGEX

# Returns a list of all matches
print(re.findall('match', 'a match test phrase where match is in the middle and also in the end match'))

# REGEX PATTERN SYNTAX


def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print(f'Searching the phrase using the re check: {pattern}')
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd--sssddd---sdddsddd---dsds---dsssss---sdddd'

test_patterns = ['sd*',     # s and 0+ d's
                 'sd+',      # s and 1+ d's
                 'sd?',      # s and 0 or 1 d
                 'sd{3}',    # s and 3 d's
                 'sd{2,3}',  # s and 2-3 d's
                 ]

multi_re_find(test_patterns, test_phrase)

# REGEX CHARACTER SETS --> [abc]

test_patterns = ['[sd]',    # s or d
                 's[sd]+']  # s and 1+ s or d

multi_re_find(test_patterns, test_phrase)

# REGEX EXCLUSIONS --> [^abc]

test_phrase = 'This is a string! But it has puntiation. How can we remove it?'

print(re.findall('[^!.? ]+', test_phrase))

# REGEX CHARACTER RANGES --> [A-Z]

test_phrase = 'This is an example sentence. Lets see if we can find som letters.'

test_patterns = ['[a-z]+',      # lower case letters
                 '[A-Z]+',      # upper case letters
                 '[a-zA-Z]+',   # both lower and upper case letter
                 '[A-Z][a-z]+']  # one upper case letter followed by one lower case letter
multi_re_find(test_patterns, test_phrase)


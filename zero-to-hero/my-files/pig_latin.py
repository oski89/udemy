# Pig latin

# If word starts with a vowel, add 'ay' to the end
# If not, put first letter last and add 'ay' to the end


def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'


print(pig_latin('word'))
print(pig_latin('apple'))

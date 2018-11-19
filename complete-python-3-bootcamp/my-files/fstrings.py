
# person = {'name': 'Jenn', 'age': 23}

# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)

# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)

# for n in range(1, 11):
#     sentence = f'The value is {n:02}'
#     print(sentence)

from datetime import datetime

birthday = datetime(1989, 1, 29)

sentence = f'Oskar was born on {birthday:%A %d %B, %Y}.'
print(sentence)

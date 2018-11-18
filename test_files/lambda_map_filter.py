# Lambda


# Map
# map is like zip but for functions
def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
my_squares = list(map(square, my_nums))
print(my_squares)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(check_even, mynums)))

# Filter
# filter is like map but it only returns the True values
print(list(filter(check_even, mynums)))

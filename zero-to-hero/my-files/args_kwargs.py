
def my_args(*args):
    # Function utilizing args
    print(args)
    # Return 5 % of the sum of all arguments
    return sum(args) * 0.05


def my_kwargs(**kwargs):
    # Function utilizing kwargs
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print('I did not find any fruit here')


def my_args_kwargs(*args, **kwargs):
    # Function utilizing args and kwargs
    print(f'I would like {args[0]} {kwargs["food"]}')


print(my_args(40, 60, 50, 100))
print(my_kwargs(fruit='orange', veggie='lettuce', meat='beef'))
print(my_args_kwargs(10, 20, 30, fruit='orange', food='eggs', animal='dog'))

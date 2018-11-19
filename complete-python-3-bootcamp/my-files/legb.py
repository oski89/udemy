# LEGB - Ther order of assignment
# L = Local (inside function)
# E = Enclosing function locals (inside function of function)
# G = Global
# B = Built-in

# It is often better to take in local arguments and return them rather than make variables global

x = 'GLOBAL'


def func():
    x = 'ENCLOSING'

    def hello():
        x = 'LOCAL'
        print(f'x is a {x} variable')
    hello()


func()

y = 50


def func2():
    global y
    print(f'y is {y}')

    y = 200
    print(f'I just locally changed global y to {y}')


func2()
print(f'y is {y}')

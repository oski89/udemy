class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def sleep(self):
        print('I am sleeping')

    def eat(self):
        print('I am eating')

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog():

    species = 'mammal'

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots

    def bark(self):
        if self.spots:
            spot_str = ' don\'t'
        else:
            spot_str = ''
        print(f'Woof! My name is {self.name} and I{spot_str} have spots.')

    def speak(self):
        return f'{self.name} says woof!'


class Cat():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('I am a cat and I\'m eating')

    def speak(self):
        return f'{self.name} says meow!'


class Horse(Animal):

    def __init__(self, name):
        Animal.__init__(self)
        self.name = name

    def sleep(self):
        print(f'I am {self.name} the horse and I\'m sleeping')

    def eat(self):
        print(f'I am {self.name} the horse and I\'m eating')


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages


# Attributes and methods
elsa = Dog(breed='Westie', name='Elsa', spots=False)
elsa.bark()
nisse = Cat('Nisse')
nisse.eat()

# Inheritance
sven = Horse('Sven')
sven.sleep()
sven.eat()

# Polymorphism
for pet in [elsa, nisse]:
        print(pet.speak())

# Utilizing built-in functions
book = Book('Factufulness', 'Hans Rosling', 500)
print(book)
print(len(book))

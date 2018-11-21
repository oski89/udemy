class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def sleep(self):
        print('I am sleeping')

    def eat(self):
        print('I am eating')


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
        print('Woof! My name is {} and I{} have spots.'.format(self.name, spot_str))


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)

    def eat(self):
        print('I am a cat and I\'m eating')


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages


dog = Dog(breed='Westie', name='Elsa', spots=False)
dog.bark()

cat = Cat()
cat.eat()

book = Book('Factufulness', 'Hans Rosling', 500)
print(book)
print(len(book))

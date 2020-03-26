# Duck Typing and Easier to ask forgiveness than permission (EAFP)

my_file = 'test.txt'

# No Race-Condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())

person = {'name': 'Adama', 'job': 'Entrepreneur', 'age': 33}
# person = {'name': 'Adama', 'age': 33}
print()

# EAFP (pythonic)
try:
    print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}")
except KeyError as e:
    print(f'Missing {e} key.')

print()


my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')


# The only problem I see here, is that I have to know all Error-Types, now.
# Meaning, which error (or its corresponding literal) do I have to catch in the exception part.

# I usually throw errors manually,
# i.e. commit errors deliberately so that the compiler complains and throws an exception with its name.


class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


# d = Duck()
# quack_and_fly(d)
#
# p = Person()
# quack_and_fly(p)

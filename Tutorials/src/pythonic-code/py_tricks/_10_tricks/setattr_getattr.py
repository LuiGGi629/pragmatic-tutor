class Person:
    pass


person = Person()

first_key = 'first'
first_val = 'Adama'

setattr(person, first_key, first_val)
first = getattr(person, first_key)
# print(first)

person_info = {'first': 'Adama', 'last': 'Jimenez'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

# print(person.first)
# print(person.last)

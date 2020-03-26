import itertools
import operator
import os

from snippets import letters, numbers, names, selectors, people

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials/src/pythonic-code/py_tricks/iteration/iter-tools')

# counter = itertools.count(start=5, step=-2.5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]
#
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

# counter = itertools.cycle(('On', 'Off'))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# squares = map(pow, range(10), itertools.repeat(2))
# print(list(squares))

# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
# print(list(squares))

# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)

# result = itertools.product(numbers, repeat=4)
# result = itertools.combinations_with_replacement(numbers, 4)
# for item in result:
#     print(item)

# combined = itertools.chain(letters, numbers, names)
# for item in combined:
#     print(item)

# result = itertools.islice(range(10), 1, 5, 2)
# for item in result:
#     print(item)

# with open('test.log', 'r') as f:
#     header = itertools.islice(f, 3)
#
#     for line in header:
#         print(line, end='')


def lt_2(n):
    if n < 2:
        return True
    return False


# result = filter(lt_2, numbers)

# result = itertools.filterfalse(lt_2, numbers)

# result = itertools.dropwhile(lt_2, numbers)

# result = itertools.takewhile(lt_2, numbers)

# result = itertools.compress(letters, selectors)

# result = itertools.accumulate(numbers, operator.mul)
#
# for item in result:
#     print(item)


def get_state(person):
    return person['state']


# @TODO sort people dict

sorted_people = sorted(people, key=get_state)

person_group = itertools.groupby(sorted_people, get_state)

# person_group = itertools.groupby(people, get_state)

# copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

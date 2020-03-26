import datetime
import random

import memory_profiler

# my_nums = (n * n for n in [1, 2, 3, 4, 5])

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (before): {memory_profiler.memory_usage()} in MiB')


def ppl_list(num_ppl):
    result = []
    for i in range(num_ppl):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)

    return result


def ppl_gen(num_ppl):
    for i in range(num_ppl):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


t0 = datetime.datetime.now()
people = ppl_gen(1_000_000)
t1 = datetime.datetime.now()

print(f'Memory (after): {memory_profiler.memory_usage()} in MiB')
print(f'Took {(t1-t0).total_seconds():.2f} sec.')

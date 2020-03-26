# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)


my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

# Set Comprehensions
# nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
# my_set = {n for n in nums}
# print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def gen_func(numbers):
#     for num in numbers:
#         yield num * num
#
#
# my_gen = gen_func(nums)
# for n in my_gen:
#     print(n)

my_gen = (n * n for n in nums)
for num in my_gen:
    print(num)

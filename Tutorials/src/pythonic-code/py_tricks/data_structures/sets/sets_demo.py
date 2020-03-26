employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# result = set(gym_members).intersection(developers)
result = set(employees).difference(developers, gym_members)

print(result)

if 'Jane' in developers:
    print('Found!')

# (O)n for list
# O(n) for a set!

# l1 = [1, 2, 3, 1, 2, 3]
# l2 = list(set(l1))
# print(l2)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = {3, 4, 5}

# s4 = s1.intersection(s2, s3)
# s4 = s1.difference(s2)
# s4 = s1.symmetric_difference(s2)
#
# print(s4)

# empty_set = set()
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {5, 10, 12, 14}
# s1.add(6)
# s1.update([7, 8, 9], s2)
# s1.remove(12)
#
# try:
#     s1.remove(12)
# except KeyError as e:
#     print('This key is missing')
#
# s1.discard(14)
# # discard does not throw key error when value does not exist
# s1.discard(14)
#
# print(s1)

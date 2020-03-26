names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))
print(identities)

for identity in identities:
    print(f'{identity[0]} is {identity[1]}')

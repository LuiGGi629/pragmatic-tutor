from operator import attrgetter

nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]

sorted_nums = sorted(nums, reverse=True)

print(f"Original Variable:\t{nums}")

print(f"Sorted Variable:\t{sorted_nums}")

nums.sort()

print(f"Sort Method:\t{nums}")

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

sorted_tup = sorted(tup)

print(f"Sorted Tuple:\t{sorted_tup}")

my_dict = {'name': 'Wojtas', 'job': 'programista za niecałe 300 czyli za 200', 'age': None, 'os': 'Mac', }

sorted_dict = sorted(my_dict)

print(f"Sorted Dict:\t{sorted_dict}")

li = [-6, -5, -4, 3, 2, 1]
s_li = sorted(li)
print(f'Default Sort:\t{s_li}')

abs_li = sorted(li, key=abs)

print(f'abs Sort:\t{abs_li}')


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary:,})'


e1 = Employee('Carl', 43, 78000000)
e2 = Employee('Violet', 33, 890000000)
e3 = Employee('Sylvia', 37, 98000000000)

employees = [e1, e2, e3]


# def emp_sort(emp):
#     return emp.salary


# sorted_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
sorted_employees = sorted(employees, key=attrgetter('salary'), reverse=True)
print(sorted_employees)


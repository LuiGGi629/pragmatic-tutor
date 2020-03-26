class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f'Employee({self.first} - {self.last} - {self.pay:,})'

    def __str__(self):
        return f'{self.full_name()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Adama', 'Trałore', 200_000)
emp_2 = Employee('Raul', 'Himenes', 300_000)

print(repr(emp_1))
print(str(emp_1))

print(f'{emp_1 + emp_2:,}')
print(len(emp_1), len(emp_2))

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@wolves.pl'

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


print(Employee.num_of_emps)

emp_1 = Employee('Adama', 'Trałore', 200_000)
emp_1.apply_raise()
print(f'{emp_1.pay:,}')
emp_2 = Employee('Raul', 'Himenes', 300_000)

print(Employee.num_of_emps)

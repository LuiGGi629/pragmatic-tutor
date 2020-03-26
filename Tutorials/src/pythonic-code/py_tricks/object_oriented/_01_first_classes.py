class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@wolves.pl"

    def full_name(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Adama', 'Trałore', 200_000)
emp_2 = Employee('Raul', 'Himenes', 200_000)
print(emp_1.full_name())
print(emp_1.email)
print(emp_1.pay)
print(emp_2.email)

emp_1.full_name()
print(Employee.full_name(emp_1))  # background

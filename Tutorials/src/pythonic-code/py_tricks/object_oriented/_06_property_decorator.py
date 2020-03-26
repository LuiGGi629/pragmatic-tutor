class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Chris', 'Bąk')
emp_1.full_name = 'Jimmy Byk'
print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)
del emp_1.full_name
print(emp_1.full_name)
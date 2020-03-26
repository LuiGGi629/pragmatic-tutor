import sqlite3

from employee import Employee

# conn = sqlite3.connect('employee.db')

# useful for creating fresh empty db for testing
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("UPDATE employees SET pay = :pay WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp1 = Employee('John', 'Doe', 80000)
emp2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp2, 95000)
remove_emp(emp1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()

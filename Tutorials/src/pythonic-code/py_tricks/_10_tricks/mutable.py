import time
from datetime import datetime


def display_time_bad(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))


print(display_time_bad.__defaults__)
display_time_bad()
time.sleep(1)
display_time_bad()
time.sleep(1)
display_time_bad()


def display_time_good(time_to_print=None):
    if not time_to_print:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))


print(display_time_good.__defaults__)
display_time_good()
time.sleep(1)
display_time_good()
time.sleep(1)
display_time_good()


# def add_employee_bad(emp, emp_list=[]):
#     emp_list.append(emp)
#     print(emp_list)
#
#
# print(f'bad: {add_employee_bad.__defaults__}')
# add_employee_bad('Adama')
# print(f'emp list not emp: {add_employee_bad.__defaults__}')
# add_employee_bad('Raul')
# print(f'emp list not emp: {add_employee_bad.__defaults__}')
#
#
# def add_employee_good(emp, emp_list=None):
#     if emp_list is None:
#         emp_list = []
#     emp_list.append(emp)
#     print(emp_list)
#
#
# print(f'good: {add_employee_good.__defaults__}')
# emps = ['John', 'Jane']
# add_employee_good('Adama', emps)
# print(f'good: {add_employee_good.__defaults__}')
# add_employee_good('Jerry')

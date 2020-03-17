import os

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')

data = pd.read_csv('data/age_all_py_js.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287
plt.fill_between(ages, py_salaries, dev_salaries, where=py_salaries > dev_salaries,
                 interpolate=True, alpha=0.25, label='Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, where=py_salaries <= dev_salaries,
                 interpolate=True, alpha=0.25, label='Below Avg')

plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.savefig('pics/mpl-plots/fill_line_plot')
plt.show()

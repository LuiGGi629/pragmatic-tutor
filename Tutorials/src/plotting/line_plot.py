import os
from matplotlib import pyplot as plt
from snippets import ages_x_18_55, py_dev_y_18_55, js_dev_y_18_55, dev_y_18_55

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')
plt.style.use('fivethirtyeight')

plt.plot(ages_x_18_55, py_dev_y_18_55, label='Python')
plt.plot(ages_x_18_55, js_dev_y_18_55, label='JavaScript')
plt.plot(ages_x_18_55, dev_y_18_55, color='#444444', linestyle='--', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.tight_layout()
# plt.savefig('pics/mpl-plots/line_median_salary_18_55.png')
plt.show()

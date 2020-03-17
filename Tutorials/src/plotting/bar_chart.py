import os
import numpy as np
from matplotlib import pyplot as plt
from snippets import dev_y, ages_x, js_dev_y, py_dev_y

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')
plt.style.use('fivethirtyeight')

x_indexes = np.arange(len(ages_x))
width = 0.25

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', linestyle='--', label='All Devs')
plt.bar(x_indexes, py_dev_y, width=width, label='Python')
plt.bar(x_indexes + width, js_dev_y, width=width, label='JavaScript')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.tight_layout()
plt.savefig('pics/mpl-plots/bar_median_salary_25_35.png')
plt.show()

import os

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')

data = pd.read_csv('data/id_age.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor='black', log=True)
median_age = 29
color = '#fc4f30'
plt.axvline(median_age, color=color, label='Age Median', linewidth=2)
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('pics/mpl-plots/hist_ages.png')
plt.show()

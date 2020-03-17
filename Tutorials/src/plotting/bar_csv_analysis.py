import os
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')

data = pd.read_csv('data/languages.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages, popularity = map(list, zip(*language_counter.most_common(15)))

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')
plt.tight_layout()
# plt.savefig('pics/mpl-plots/h_bar_most_pop_lang.png')
plt.show()

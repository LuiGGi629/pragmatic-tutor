import os

from matplotlib import pyplot as plt
from snippets import slices, labels

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')
plt.style.use('fivethirtyeight')
explode = [0, 0, 0, 0.2, 0]
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, explode=explode,
        shadow=True, startangle=90, autopct='%1.1f%%')
plt.title('Popularity')
plt.tight_layout()
plt.savefig('pics/mpl-plots/pie_lang_popularity.png')
plt.show()

import os
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')

data = pd.read_csv('data/views_likes_ratio.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolors='black',
            linewidths=1, alpha=0.70)
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
plt.xscale('log')
plt.yscale('log')
plt.title('Top 200 YouTube Trending Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
# plt.savefig('pics/mpl-plots/scatter_plot.png')
plt.show()

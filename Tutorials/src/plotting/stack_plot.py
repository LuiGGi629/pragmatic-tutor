import os

from matplotlib import pyplot as plt

from snippets import player3, player2, player1, minutes

os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')
plt.style.use('fivethirtyeight')
labels = ['player1', 'player2', 'player3']
plt.stackplot(minutes, player1, player2, player3, labels=labels)
plt.legend(loc='upper left')
plt.title('Stack Plot')
plt.tight_layout()
plt.savefig('pics/mpl-plots/stack_plot.png')
plt.show()

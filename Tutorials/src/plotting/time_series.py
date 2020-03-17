import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('fivethirtyeight')
os.chdir('/Users/wojtek/PycharmProjects/pragmatic-tutor/Tutorials')

data = pd.read_csv('data/time_series.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d, %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.savefig('pics/mpl-plots/btc_time_series.png')
plt.show()

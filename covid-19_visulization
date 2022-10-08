#this is about visulizind daily conform cases, death, recovered and total cases 

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv',parse_dates=['Date'])
df['total cases'] = df[['Confirmed','Recovered','Deaths']].sum(axis=1)

worldwide = df.groupby(['Date']).sum()

plt.style.use('fivethirtyeight')

w = worldwide.head().plot(figsize=(16,9))
w.set_xlabel('dates')
w.set_xlabel('covid')
w.title.set_text('codiv visulazation')

plt.show()

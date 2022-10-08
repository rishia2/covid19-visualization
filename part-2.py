import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv',parse_dates=['Date'])

df['total cases'] = df[['Confirmed','Recovered','Deaths']].sum(axis=1)

us_df = df[df['Country']=='US'].groupby(['Date']).sum()

fig=plt.figure(figsize=(25,6))
ax=fig.add_subplot(111)

ax.plot(worldwide[['total cases']],label='world')
ax.plot(us_df[['total cases']],label='us')

ax.set_xlabel('dates')
ax.set_xlabel('covid')
ax.title.set_text('codiv visulazation')

plt.legend(loc='upper left')

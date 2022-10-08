import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv',parse_dates=['Date'])

df['total cases'] = df[['Confirmed','Recovered','Deaths']].sum(axis=1)

#us_df=us_df.reset_index()
us_df['daily conf'] = us_df['Confirmed'].sub(us_df['Confirmed'].shift())
us_df['daily death'] = us_df['Deaths'].sub(us_df['Deaths'].shift())

fig = plt.figure(figsize=(20,7))
ax= fig.add_subplot(111)

ax.bar(us_df['Date'].head(200),us_df['daily conf'].head(200),color='b',label='conf')
ax.bar(us_df['Date'].head(200),us_df['daily death'].head(200),color='r',label='deaths')

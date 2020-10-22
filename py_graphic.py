import pandas as pd
import matplotlib.pyplot as plt

files = ['data/gapminder_gdp_asia.csv', 
         'data/gapminder_gdp_africa.csv', 
         'data/gapminder_gdp_americas.csv']

for filename in files:
    dataframe = pd.read_csv(filename)
    dataframe.mean().plot()
plt.xticks(rotation=45)
plt.savefig('mean_gdp.png')

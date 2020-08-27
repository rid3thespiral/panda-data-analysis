import pandas as pd
import bar_chart_race as bcr
import warnings as ws
from pathlib import Path

ws.filterwarnings("ignore")

path = str(Path(__file__).parents[2])+"/materials/cssecovid19.csv"
covid19 = pd.read_csv(path)

#format dataframe to adapt to bar_chart_race
covid19.drop(["Lat", "Long"], axis=1, inplace=True)

covid19 = covid19.groupby("Country/Region").sum()
covid19 = covid19.T #index as Date
covid19.index = pd.to_datetime(covid19.index)
print(covid19)

bcr.bar_chart_race(df=covid19,
                   filename='covid.mp4',
                   n_bars=2,
                   title='casi confermati covid-19 - top 10 paesi')
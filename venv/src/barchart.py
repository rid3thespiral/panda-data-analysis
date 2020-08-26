import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

path = str(Path(__file__).parents[2])+"/materials/FB.csv"
fb = pd.read_csv(path, parse_dates=["Date"], index_col="Date").round(2)
new_index = pd.date_range(start = fb.index.min(), end=fb.index.max(), freq="D")
fb = fb.reindex(new_index, method = "ffill")

#show mean values fb stock price "Close" between may 2019 - 2020
fbmonths = fb.resample("M").mean()
fbmonths.index= fbmonths.index.month_name()
print(fbmonths)

fbmonths.plot(figsize=(16,6),kind="barh", y="Close")
plt.show()
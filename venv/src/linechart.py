import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

path = str(Path(__file__).parents[2])+"/materials/FB.csv"
fb = pd.read_csv(path, parse_dates=["Date"], index_col="Date").round(2)

new_index = pd.date_range(start = fb.index.min(), end=fb.index.max(), freq="D")
fb = fb.reindex(new_index, method = "ffill")


#line plot
#fb.plot(y = ["Open", "Close"])

#subplots
plt.style.use('seaborn-whitegrid')
fb.plot(subplots=True, figsize = (15,10), color = "r")
plt.show()
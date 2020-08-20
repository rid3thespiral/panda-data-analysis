import pandas as pd
from pathlib import Path

path1 = str(Path(__file__).parents[2])+"/materials/fifa20.csv"

altezza = pd.read_csv(path1, usecols=["player", "height_cm"], squeeze=True, index_col="player")
altezza10 = altezza.head(10)
print(altezza10)
top500 = altezza.head(500)
maxplayer = top500.idxmax()
maxplayervalue= top500.max()
print(maxplayer, maxplayervalue," cm")
minplayer = top500.idxmin()
minplayervalue = top500.min()
print(minplayer, minplayervalue," cm")
print("Altezza media: ", top500.mean().round(1), " cm")
print("Altezza M. Salah: ", top500["M. Salah"])
top500.to_csv("top500.csv", index=True)
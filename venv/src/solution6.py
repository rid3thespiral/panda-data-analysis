import pandas as pd
from pathlib import Path

pathtop20 = str(Path(__file__).parents[2])+"/materials/esercizi/top_20.csv"
pathnba1 = str(Path(__file__).parents[2])+"/materials/esercizi/nba_1.csv"
pathnba2 = str(Path(__file__).parents[2])+"/materials/esercizi/nba_2.csv"

top20= pd.read_csv(pathtop20)
nba1 = pd.read_csv(pathnba1)
nba2 = pd.read_csv(pathnba2)

print(top20.head())
print(nba1)
print(nba2)

#find teams by richest players
nba_full = nba1.append(nba2)
print(nba_full)

top20["Player"]=top20["Player"].str.replace(" ", "")

result = pd.merge(top20, nba_full, how="outer", left_on="Player", right_on="FULLNAME").drop(["FULLNAME", "POS", "AGE",  "GP", "MPG", "PPG", "RPG", "APG"], axis=1)
print(result.head(20))



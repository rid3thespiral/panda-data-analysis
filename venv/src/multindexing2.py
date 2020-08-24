import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/nba.xlsx"
nba = pd.read_excel(p, index_col=[2,1]).sort_index() #multi-index with nba["POS"] and nba["TEAM"]

#extracting index and rows from multi-index (loc)
print(nba.loc["C"])
#extracting Atlanta's centers
print(nba.loc[("C", "Atl")]) #passing a tuple
#fullname serie
print(nba.loc[("C", "Atl"), "FULLNAME"])
#fullname and games played
print(nba.loc[("C", "Atl"), ["FULLNAME", "GP"]])
#center and guards atlanta
print(nba.loc[("C", "G"), "Atl", :]) #slicing on all rows
#only atlanta players
print(nba.loc[(slice(None), slice("Atl")), :])
#using lists like dataframes
print(nba.loc[pd.IndexSlice[:, "Atl"], :])


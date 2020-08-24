import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/nba.xlsx"
nba = pd.read_excel(p)

nba.set_index("POS") #for a single-index
nba.set_index(["POS", "TEAM"], inplace=True)
nba.sort_index(inplace=True)
print(nba.index)
print(type(nba.index[0])) #is a tuple

print(nba.index.get_level_values(1))
print(nba.swaplevel()) #good practice to have external index with less unique values



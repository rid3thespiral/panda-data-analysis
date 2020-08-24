import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/titanic.csv"
titanic = pd.read_csv(p, index_col="Name")

titanic.index = titanic.index.str.upper()
print(titanic)
titanic.columns = titanic.columns.str.upper()
print(titanic)
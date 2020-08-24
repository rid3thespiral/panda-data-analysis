import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/titanic.csv"
df = pd.read_csv(p)
print(df.tail())

titanic = df.copy()
print(titanic)

titanic.set_index(keys = ["Pclass", "Sex"], inplace=True)

print(titanic.agg(({"Fare": ["max", "min"], "Age":["max", "min"]})))

print(titanic.loc[(1, "male"), :])

print(titanic.reset_index(inplace = True))
titanic["Sex"] = titanic["Sex"].str.title()
titanic.set_index(keys = ["Pclass", "Sex"], inplace=True)
print(titanic)
import pandas as pd
from pathlib import Path

#merge method
#7 kind of joins, like in SQL
#outer join
p = str(Path(__file__).parents[2])+"/materials/bos_2019.xlsx"
p2 = str(Path(__file__).parents[2])+"/materials/bos_2020.xlsx"
bos_2019 = pd.read_excel(p)
bos_2020 = pd.read_excel(p2)

#both dfs with the same TEAM values, dropping columns
bos_2019.drop("TEAM", axis=1, inplace=True)
bos_2020.drop("TEAM", axis=1, inplace=True)

#union: outer join
print(pd.merge(bos_2019,bos_2020, how="outer", on="FULLNAME", suffixes=('_2019', '_2020'), indicator=True))

#intersection: inner join
#reading dataframes
bos_2019 = pd.read_excel(p, usecols=["FULLNAME", "MPG"])
bos_2020 = pd.read_excel(p2, usecols=["FULLNAME", "MPG"])
print(bos_2019.merge(bos_2020, how="inner", on="FULLNAME", suffixes=('_2019', '_2020')))

#left and right join (with intersection)
print(bos_2019.merge(bos_2020, how="left", on="FULLNAME", suffixes=('_2019', '_2020'), indicator=True))
print(bos_2019.merge(bos_2020, how="right", on="FULLNAME", suffixes=('_2019', '_2020'), indicator=True))

#left and right join (without intersection)
bos=bos_2019.merge(bos_2020, how="outer", on="FULLNAME", suffixes=('_2019', '_2020'), indicator=True)
print(bos[bos["_merge"] == 'left_only'])
print(bos[bos["_merge"] == 'right_only'])

#outer join without intersection
bos=bos_2019.merge(bos_2020, how="outer", on="FULLNAME", suffixes=('_2019', '_2020'), indicator=True)
print(bos[bos["_merge"] != 'both'])

#merge on cols with different names
bos_2020 = pd.read_excel(p2, usecols=["FULLNAME", "POS"])
bos_2020.rename(columns={"FULLNAME":"NAME"},inplace=True)
print(pd.merge(bos_2019, bos_2020, how="inner", left_on="FULLNAME", right_on="NAME").drop("NAME", axis=1))

#merge on axis with different names
bos_2019=pd.read_excel(p, usecols=["FULLNAME", "POS"])
bos_2020=pd.read_excel(p2, usecols=["FULLNAME", "MPG"], index_col="FULLNAME")
bos_2019.rename(columns={"FULLNAME":"NAME"},inplace=True)
print(bos_2019.head())
print(bos_2020.head())

print(pd.merge(bos_2019, bos_2020, how="inner", left_on="NAME", right_index=True))

#join(): covered by merge()
bos_2020=pd.read_excel(p2, usecols=["FULLNAME", "POS"], index_col="FULLNAME")
bos_2019=pd.read_excel(p, usecols=["FULLNAME", "MPG"], index_col="FULLNAME")
print(pd.merge(bos_2019, bos_2020, how="inner", left_index=True, right_index=True))
print(bos_2019.join(bos_2020, how="inner")) #same risult

#append covered by concat and join covered by merge()


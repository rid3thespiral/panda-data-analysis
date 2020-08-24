import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/titanic.csv"
titanic = pd.read_csv(p)

#transpose method
print(titanic.T)
print(titanic.T.T)

#pay attention to dtypes
titanic.info() #many dtypes
titanic.T.info()
titanic.T.T.info() #object dtypes

#stack() and unstack()
titanic = pd.read_csv(p, index_col = "Name", usecols = ["Name", "Pclass", "Sex", "Age"])
print(titanic)

#stack(): takes colnames and put as index (Multi-index) from 891*3 -> 3*839*1
print(titanic.stack(dropna=True))

#unstack(): stack opposite()
titanic = pd.read_csv(p, index_col = ["Pclass", "Name"], usecols = ["Name", "Pclass", "Sex", "Age"]).head()
print(titanic.unstack(level = 0))

#melt(): wide to long transformation
p = str(Path(__file__).parents[2])+"/materials/pop.xlsx"
pop = pd.read_excel(p)
print(pop)
print(pop.melt()) #wide to long transformation
print(pop.melt(id_vars = "Country Name", var_name="year", value_name="population", value_vars=[2016,2017,2018,2019]))

#pivot(): long to wide transformation
p = str(Path(__file__).parents[2])+"/materials/salaries.csv"
dfsal = pd.read_csv(p)
print(dfsal) #55 rows x 3 columns
print(dfsal.pivot(index = "Season", columns="Player", values="Salary").fillna("No games"))

#pivot_table(): same in Excel. More than pivot(), can accept aggfunc
p = str(Path(__file__).parents[2])+"/materials/disoccupati.csv"
disocc = pd.read_csv(p)
print(disocc)
print(disocc["TIME"].value_counts())

print(disocc.pivot_table(values="Value", index="TIME", columns="Territorio",aggfunc = 'sum' ))
print(disocc.pivot_table(values="Value", index="TIME", aggfunc = 'sum' ))
print(disocc.pivot_table(values="Value", index="TIME", columns="Cittadinanza",aggfunc = 'sum' ))
print(disocc.pivot_table(values="Value", index=["Territorio", "TIME"], columns="Cittadinanza", aggfunc = 'sum' ))

#groupby: split, apply, combine paradigm
p = str(Path(__file__).parents[2])+"/materials/residenti.csv"
df = pd.read_csv(p)

regioni = df.groupby(by = "Territorio") #split
print(regioni.get_group("Basilicata"))

#total population by regione
print(df.pivot_table(index="Territorio", values="Value", aggfunc="sum"))
print(regioni.sum())

#groupby by columns
regioni_stato_civile = df.groupby( by = ["Territorio", "Stato civile"]) #split
regioni_stato_civile.groups #20 * 5 multi-index dataframe indexed by tuples
print(regioni_stato_civile.sum())
#the same of regioni_stato_civile.sum()
print(df.pivot_table(index = ["Territorio", "Stato civile"], values="Value", aggfunc="sum"))

#number of > 100 years people by "Territorio"
centenari= df.groupby(["Territorio", "Età"]).sum()
print(centenari.loc[(slice(None), "100 anni e più"), :].sort_values(by="Value", ascending=False))
#same
centenari2 = centenari.pivot_table(index=["Territorio", "Età"], values="Value", aggfunc="sum")
print(centenari2.loc[(slice(None), "100 anni e più"), :])



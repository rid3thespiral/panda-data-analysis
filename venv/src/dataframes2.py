import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/titanic.csv"
titanic = pd.read_csv(p)
titanic.head(10)
print(titanic.info())

#1. Display passengers in the first class
mask = titanic["Pclass"] == 1
print(titanic[mask])
#alternative method that servers also Nan values
print(titanic.where(titanic["Pclass"] == 1))
#alternative method that substitutes Nan with Falso string
print(titanic.where(titanic["Pclass"] == 1, other = 'Falso'))
#query needs a string to be evaluated, dropping Nan rows (same output as first point)
print(titanic.query("Pclass == 1"))

#aggregation agg() - custom stats
titanic.describe(include = "all")

print(titanic.agg("max"))
print(titanic.agg(["max", "min"]))

#use it with dictionaries
print(titanic.agg(({"Fare": "max", "Age":["max", "min", "mean"]})))

#copy method
print(titanic["Age"])

age = titanic["Age"].copy()
age[0] = 1000;
print(age[0] == titanic["Age"][0], "Disjoint copy")

#names copy, string functions
nomi = titanic["Name"].head(10).copy()
stringa = "My name is Jack"
print(stringa.upper())
print(nomi.str.upper())
print(nomi.str.lower())
print(nomi.str.title())
print(nomi.str.len())
print(nomi.str.contains("Mr")) #returns boolean values
#filtering
print(nomi[nomi.str.contains("Mr")])

#normalize
nomi.str.lower().str.contains("mrs")
#not normalize
nomi.str.lower().str.contains("mrs", case = False)

#operations with strings
#startswith()
nomi.str.startswith("A")
#replace
nomi.str.replace("Mr.", "Mister", regex=False)
#split() and get()
print(nomi.str.split(","))
#obtaining surname
print(nomi.str.split(",").str.get(0))
print(nomi.str.split(",", expand=True))






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
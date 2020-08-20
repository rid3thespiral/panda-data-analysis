import pandas as pd
from pathlib import Path

letters = ['a', 'e', 'i', 'o', 'u']
numbers = [10,20,30,40,50]
s1 = pd.Series(letters)
s2 = pd.Series(numbers)
print(s1, s2)

#attributes
print(s1.dtype, s2.values)
print(s2.dtype, s2.values)
print(s1.index)
print(s1.shape, s1.size)
print(s2.shape, s2.size)

#methods
s = pd.Series([1.2, 3.5, 2.8, 2.5])
print(s.max())
print(s.min())
print(s.sum())
print(s.idxmax())
print(s.idxmin())
print(s.round())
p = str(Path(__file__).parents[2])+"/materials/fifa20.csv"
fifa_names = pd.read_csv(p)
fifa_names_series = pd.read_csv(p, usecols=["player"], squeeze= True) #extracting data series from csv file
#output in csv file
fifa_names.to_csv("prova.csv", index=False)

firstenplayers= fifa_names_series.head(10) #extract first N lines
fifa_names.tail(10) #extract last N lines
fifa_names_firsts = pd.read_csv(p, nrows=5) #great datasets

fifa_names_series.sort_values(axis=0, ascending=False, inplace=False, kind='quicksort', ignore_index=False) #sorting by values
fifa_names_series.sort_index(ascending=False)

print(fifa_names_series.value_counts(normalize=False, sort=True, ascending=False)) #counting occurences

fifa_ratings = pd.read_csv(p, usecols=["rating"],squeeze=True)
print(fifa_ratings.value_counts(bins = 5)) #divides data in subgroups

#extracting values by position or by slicing
print(firstenplayers[0]) #position0
print(firstenplayers[[0,2,5]])
print(firstenplayers[2:6])

#access by index
pl_ratings = pd.read_csv(p, usecols=["player", "rating"], index_col = "player", squeeze=True);
pl_ratings = pl_ratings.head(10)
print(pl_ratings["L. Messi", "Neymar Jr"]) #generating a new series

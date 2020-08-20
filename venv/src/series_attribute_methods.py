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
print(pd.read_csv(p))
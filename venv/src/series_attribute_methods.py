import pandas as pd

letters = ['a', 'e', 'i', 'o', 'u']
numbers = [10,20,30,40,50]
s1 = pd.Series(letters)
s2 = pd.Series(numbers)
print(s1, s2)

#attributes
print(s1.dtype, s2.values)
print(s2.dtype, s2.values)
print(s1.index)


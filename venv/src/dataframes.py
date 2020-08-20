import pandas as pd
from pathlib import Path

#building a dataframe from dictionaries
d1 = {'col1': [1,2,3], 'col2': [4,5,6], 'col3': [7,8,9]}
df1 = pd.DataFrame(data=d1)
print(df1)

#each column is a panda Series
print(type(df1["col1"]))

#building a dataframe from lists
df2 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=["i1", "i2", "13"], columns=['a','b','c'])
print(df2)

#attributes
p = str(Path(__file__).parents[2])+"/materials/fifa20.csv"
fifa = pd.read_csv(p)
print("Info about fifa dataframe: ")
print(fifa.shape)
print(fifa.columns)
print(fifa.axes)
print(fifa.dtypes)
print(fifa.values)

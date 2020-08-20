import pandas as pd

#creating series with pandas constructor
#lists


list2 = ['a', 'e', 'i', 'o', 'u']
print(pd.Series(data = list2))
print(pd.Series(data = list2, index=[10,20,30,40,50]))

#index different from a number
print(pd.Series(data = list2, index=['vocal1', 'vocal2', 'vocal3', 'vocal4', 'vocal5']))

#using dictionaries
dict1 = {"name": 'jack', "surname": 'sparrow', "country": 'brasil'}
print(pd.Series(data = dict1))

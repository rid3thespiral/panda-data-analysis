import pandas as pd
from pathlib import Path

#join, concatenate and merge dataframes
#case1: same index between dfs
df1 = pd.DataFrame({"A" : ["A0", "A1", "A2", "A3"],
                    "B" : ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]})

df2 = pd.DataFrame({"A" : ["A4", "A5", "A6", "A7"],
                    "B" : ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]})

df3 = pd.DataFrame({"A" : ["A8", "A9", "A10", "A11"],
                    "B" : ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]})

print(pd.concat(objs=[df1,df2,df3], keys=["df1", "df2", "df3"]))
print(pd.concat(objs=[df1,df2,df3], keys=["df1", "df2", "df3"], ignore_index=True))
print(pd.concat(objs=[df1,df2,df3], axis=1, keys=["df1", "df2", "df3"])) #concat by columns

#case2: different indexes
df2 = pd.DataFrame({"A" : ["A4", "A5", "A6", "A7"],
                    "B" : ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]}, index=[4,5,6,7])

df3 = pd.DataFrame({"A" : ["A8", "A9", "A10", "A11"],
                    "B" : ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]}, index=[8,9,10,11])

print(pd.concat(objs=[df1,df2,df3]))
print(pd.concat(objs=[df1,df2,df3], axis=1)) #filled with NaN

#case3: label columns different
df1 = pd.DataFrame({"A" : ["A0", "A1", "A2", "A3"],
                    "B" : ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]})

df2 = pd.DataFrame({"E" : ["A4", "A5", "A6", "A7"],
                    "F" : ["B4", "B5", "B6", "B7"],
                    "G": ["C4", "C5", "C6", "C7"],
                    "H": ["D4", "D5", "D6", "D7"]})

df3 = pd.DataFrame({"I" : ["A8", "A9", "A10", "A11"],
                    "L" : ["B8", "B9", "B10", "B11"],
                    "M": ["C8", "C9", "C10", "C11"],
                    "N": ["D8", "D9", "D10", "D11"]})

print(pd.concat([df1,df2,df3], axis=1))
print(pd.concat([df1,df2,df3])) #filled with NaN

#case3: label columns different and different index
df1 = pd.DataFrame({"A" : ["A0", "A1", "A2", "A3"],
                    "B" : ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]}, index=[0,1,2,3])

df2 = pd.DataFrame({"E" : ["A4", "A5", "A6", "A7"],
                    "F" : ["B4", "B5", "B6", "B7"],
                    "G": ["C4", "C5", "C6", "C7"],
                    "H": ["D4", "D5", "D6", "D7"]}, index=[4,5,6,7])

df3 = pd.DataFrame({"I" : ["A8", "A9", "A10", "A11"],
                    "L" : ["B8", "B9", "B10", "B11"],
                    "M": ["C8", "C9", "C10", "C11"],
                    "N": ["D8", "D9", "D10", "D11"]}, index=[8,9,10,11])

print(pd.concat([df1,df2,df3])) #filled with NaN
print(pd.concat([df1,df2,df3], axis=1)) #filled with NaN
print(df1.append([df2,df3])) #same result

#join parameter
df1 = pd.DataFrame({"A" : ["A0", "A1", "A2", "A3"],
                    "B" : ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]})

df2 = pd.DataFrame({"A" : ["A4", "A5", "A6", "A7"],
                    "B" : ["B4", "B5", "B6", "B7"],
                    "X": ["C4", "C5", "C6", "C7"],
                    "Y": ["D4", "D5", "D6", "D7"]})

print(pd.concat([df1,df2], join="inner", ignore_index=True)) #join only columns on the same key



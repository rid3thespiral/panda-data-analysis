import pandas as pd
from pathlib import Path

#adapting dimensions

s1 = pd.Series(data = [1,2,3])
s2 = pd.Series(data = [2,3,4])
print(s1+s2)

s3 = pd.Series(data = [4,5,6,9])
print(s1+s3) #with NaN broadcasting

print(s3*5) #element-wise operation


import pandas as pd
import xlrd as xlrd
import openpyxl as opyxl
from pathlib import Path

pathnba = str(Path(__file__).parents[2])+"/materials/nba.xlsx"
nba = pd.read_excel(pathnba, index_col="FULLNAME")
print(nba)
print(nba["PPG"].hasnans)

length = len(nba["PPG"])
sum = nba["PPG"].sum()
mean = sum/length
mean = round(mean,2)

nba["PPG"].fillna(mean, inplace=True)
print(nba["PPG"].hasnans)

print(nba.sort_values(axis=0,by="PPG",ascending=False).head(10))

nba["TOT"] = nba["PPG"] * nba["GP"]
print(nba.iloc[-1][2])
print(nba.iloc[0][2])

nbabymean = nba.sort_values(axis=0,by="PPG",ascending=False)
mask = nbabymean["GP"] < 30
print(nbabymean[mask].head(3))

maskt1 = "Mia"
maskt2 = "Bos"
maskt3 = "Lal"
maskt4 = "Lac"
mask = nba["TEAM"].isin([maskt1, maskt2, maskt3, maskt4])
nba2 = nba[mask]
print(nba2["AGE"].between(25,30))

mvpc = nba["PPG"] + nba["APG"] + nba["RPG"]
mvpc_sorted = mvpc.sort_values(axis=0, ascending=False, inplace=False, kind='quicksort')
print(mvpc_sorted.head(5))
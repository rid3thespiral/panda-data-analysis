import pandas as pd
import xlrd as xlrd
import openpyxl as opyxl
from pathlib import Path

#building a dataframe from dictionaries
d1 = {'col1': [1,2,3], 'col2': [4,5,6], 'col3': [7,8,9]}
df1 = pd.DataFrame(data=d1)
#print(df1)

#each column is a panda Series
#print(type(df1["col1"]))

#building a dataframe from lists
df2 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=["i1", "i2", "13"], columns=['a','b','c'])
#print(df2)

#attributes
p = str(Path(__file__).parents[2])+"/materials/fifa20.csv"
fifa = pd.read_csv(p)
#print("Info about fifa dataframe: ")
#print(fifa.shape)
#print(fifa.columns)
#print(fifa.axes)
#print(fifa.dtypes)
#print(fifa.values)

#methods
#print(df2.sum()) #sum my rows
#print(df2.sum(axis=1)) #sum by columns

#describe e info
p2 = str(Path(__file__).parents[2])+"/materials/nba.xlsx"
nba = pd.read_excel(p2)
nba_info = [nba.info(), nba.describe()] #info and stats about nba dataframe
#describe() including str parameters
nba.describe(include="all")

#nlargest, nsmallest and sort_values
nba.nlargest(n=10,columns=["AGE"],keep="last") #keep: redick higher than barea by index
nba.nlargest(n=10,columns=["GP"],keep="all") #keep all: show all duplicates
nba.nlargest(n=10,columns=["GP","AGE"],keep="all")
nba.nsmallest(n=10,columns=["GP","AGE"],keep="all")

#the same behaviour with sort_values but less efficient
nba.sort_values(by = "AGE").head(5)

#to move index in columns
#equal to pd.read_excel with index_col = "FULLNAME"
print(nba.set_index("FULLNAME", drop= True, inplace=True))

#reset index on the dataframe
nba.reset_index(drop=False, inplace=False)

#removing columns with drop columns and labels
nba.drop(columns = ["GP", "POS"])
nba.drop(labels = ["GP", "POS"], axis=1)
nba.drop(index = "BamAdebayo", inplace = True) #remove one row
nba.drop(labels = "GraysonAllen", inplace = True)

#adding columns NAZIONE with value USA
nba.insert(loc=2, column=" NAZIONE ", value="USA")

#extract rows by index, loc method
nba.sort_index(inplace = True)
nba.loc["ZionWilliamson"]
nba.loc["AaronHoliday": "AlexCaruso"] #slicing by labels

print(nba.loc["AlHorford","POS"])
print(nba.loc["AlHorford",["GP", "PPG"]])
print(nba.loc[["AlHorford", "VinceCarter"],["GP", "PPG"]]) #returns a Dataframe object
print(nba.iloc[[0,3,5]]) #index position
print(nba.iloc[0:10]) #slicing by number index
print(nba.iloc[0, [3,4]]) #age and minutes by Aaron Gordon

#filter by condition Los Angeles Lakers
mask = nba["TEAM"] == "Lal"
print(nba[mask])
#filter by points
mask2 = nba["PPG"]>25
print(nba[mask2])
#filter by non-guard players
mask3 = nba["POS"] != "G"
print(nba[mask3])

#combining two or moremasks
mask1 = nba["AGE"] > 20
mask2 = nba["AGE"] < 25
mask3 = nba["TEAM"] == "Lal"
mask4 = nba["TEAM"] == "Bos"
print(nba[mask1 & mask2]["TEAM"])
print(nba[mask3 | mask4]) #players lal or bos
mask5 = nba["PPG"] > 20
print(nba[(mask3 | mask4) & mask5])

#between instead of masks
mask= nba["AGE"].between(18,20)
print(nba[mask])

mask= nba["PPG"].between(30,35)
print(nba[mask])

#isin, isnull and notnull on series
mask = nba["TEAM"].isin(["Atl", "Chi", "Bos"])
print(nba[mask])

#notnull and isnull for Nan values

#apply method for applying functions

def age(num):
    if num > 31:
        return "vecchio"
    elif num < 21:
        return "rookie"
    else:
        return "normale"

mask = nba["AGE"].apply(age)
nba["sel"] = mask
print(nba)

def titolare(riga):
    età = riga[3]
    minuti = riga[5]
    partite = riga[6]

    if(età < 25 and minuti > 20 and partite > 5):
        return "giovane titolare"
mask = nba.apply(titolare, axis=1)
nba["tit"] = mask
print(nba)

#methods map e applymap
nba["POS"]=nba["POS"].map({ "C" : "Centro", "C-F": "Ala Grande", "G" : "Guardia"})
print(nba["POS"])
#applymap function on dataframe element by element

print(nba.applymap(lambda x: len(str(x)) ))

#methods astype to work on big files
#reducing df size by 25%
nba["AGE"]=nba["AGE"].astype("int8")
nba["GP"]=nba["GP"].astype("int8")
nba["MPG"]= nba["MPG"].astype("float32")




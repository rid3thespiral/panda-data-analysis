import pandas as pd
import xlrd as xlrd
import openpyxl as opyxl
from pathlib import Path

path = str(Path(__file__).parents[2])+"/materials/uragani.csv"
uragani = pd.read_csv(path, index_col=0) #put column 0 as index
print(uragani.dropna()) #remove NaN
print(uragani.fillna(value = "A")) #fill Nan with letter


import pandas as pd
from pathlib import Path
import datetime

path = str(Path(__file__).parents[2])+"/materials/esercizi/steps2020.xlsx"


df = pd.read_excel(path, parse_dates={'TEMPO' : ["Date", "Time"]}, index_col="TEMPO")
print(df)
ts_max = pd.Timestamp("2020-01-15 23:59:00")
step_max = df.loc["2020-01-15 23:59:00"]
dfr=pd.DataFrame({"TEMPO": ts_max, "Steps": step_max})
dfr.set_index(keys="TEMPO")
print(dfr.transpose())







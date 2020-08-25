import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/studio.csv"
df1 = pd.read_csv(p, encoding="latin1")
print(df1)

mask = df1["Sesso"] != "totale"
dfx = df1[mask]

mask = df1["Titolo di studio"] != "totale"
dfx = df1[mask]

print(dfx.pivot_table(index=["Territorio", "TIME", "Sesso"], values="Value", aggfunc="sum"))

print(dfx.pivot_table(values="Value", index="Territorio", columns=["TIME", "Sesso"], aggfunc = 'sum' ))

print(dfx.pivot_table(values="Value", index="Territorio", columns=["TIME", "Titolo di studio"], aggfunc = 'sum' ))

print(dfx.pivot_table(values="Value", index=["Titolo di studio", "TIME"], columns=["Sesso", "Territorio"], aggfunc = 'sum' ))

print(dfx.pivot_table(values="Value", index=["Titolo di studio", "TIME"], columns=["Sesso", "Territorio"], aggfunc = 'sum' ).loc[(slice(None), 2018), :])
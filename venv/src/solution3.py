import pandas as pd
from pathlib import Path

p = str(Path(__file__).parents[2])+"/materials/fifa20.csv"

fifa = pd.read_csv(p)

fifa.rename(columns={'player' : 'giocatore', 'dob': 'data di nascita'}, inplace=True)
fifa.set_index("giocatore", inplace=True)
fifa.drop(columns="age", inplace=True)

fifa["data di nascita"] = fifa["data di nascita"].apply(lambda x: x[6:])
fifa["data di nascita"] = fifa["data di nascita"].apply(lambda x: int(x))
fifa["anni"] = 2020 - fifa["data di nascita"]


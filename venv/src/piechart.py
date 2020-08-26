import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

pop = pd.read_html("https://it.qwe.wiki/wiki/List_of_continents_by_population")[0] #array of tabs

pop["% Del pop mondiale."]=pop["% Del pop mondiale."].str.strip("%").str.strip("<").str.replace(",",".").astype("float")
labels= pop["Continente"].loc[1:6]
dims = pop["% Del pop mondiale."].loc[1:6]

plt.pie(x=dims,labels=labels, autopct="%1.2f%%")
plt.show()
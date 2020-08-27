import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

path = str(Path(__file__).parents[2])+"/materials/covid.csv"
covid = pd.read_csv(path)
print(covid.info())

covid.rename(columns = {'countriesAndTerritories': "paesi", "countryterritoryCode": "countryCode",
                        'continentExp': 'continente'}, inplace = True)
print(covid.head())

#delete useless info for my purpose
covid.drop(["day", "month", "year", "geoId", "countryCode"], axis=1, inplace=True)
print(covid.head())
covid.set_index(pd.to_datetime(covid["dateRep"], dayfirst=True), inplace=True)
print(covid.head())
covid.drop("dateRep", axis=1, inplace=True)
print(covid.head())
print(covid.index.unique())
print(covid["paesi"].nunique())
print(covid["continente"].value_counts())

covid["paesi"] = covid["paesi"].astype("category") #moving countries as categories
covid["continente"] = covid["continente"].astype("category")
covid.info() #re-sizing

#groupby countries
top_10 = covid.groupby(by= "paesi").agg({"deaths": "sum", "cases": "sum"}).nlargest(n=10, columns="cases")
print(top_10)

plt.style.use('ggplot')
top_10.plot(kind="bar", figsize= (16,6), rot=45)
plt.ylabel("Numero di casi", fontsize=12)
plt.show()

covid["% pop colpita"] = (covid["cases"] / covid["popData2018"])*100
print(covid.head())
print(covid.groupby(by= "paesi").agg({"cases": "sum", "% pop colpita": "sum"}).nlargest(n=10, columns="% pop colpita"))

#pie chart by countries
continenti = covid.groupby(by = "continente").agg({"cases":"sum","deaths":"sum"})
print(continenti)

dimensioni = continenti["cases"].iloc[:5]
labels=["Africa", "America", "Asia", "Europe", "Oceania"]
plt.pie(x=dimensioni, labels=labels, autopct="%1.0f%%", radius=0.5)
plt.show()

#italy covid
italy = covid.groupby(by="paesi").get_group("Italy").sort_index()
print(italy)

italy.plot(y=["cases","deaths"], figsize=(18,5))
plt.ylabel("Numero di casi giornalieri")
plt.show()

print(italy.nlargest(n=1,columns="cases")) #worst day

italy["accumulati"] = italy["cases"].cumsum()
print(italy)

italy.plot(y="accumulati", figsize=(16,6))
plt.ylabel("Numero di casi totali")
plt.show()
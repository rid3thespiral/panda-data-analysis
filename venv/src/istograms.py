import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

path = str(Path(__file__).parents[2])+"/materials/titanic.csv"
titanic = pd.read_csv(path, index_col="PassengerId")

#age distribution
titanic.plot(kind="hist", y="Age", bins=8)


titanic["Age"].hist(bins=8)
plt.show()
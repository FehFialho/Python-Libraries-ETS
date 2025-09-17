import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("../Pandas/data/titanic.csv", sep=",")

newIndex = range(0, 11)


def total(line):
    return line["SibSp"] + line["Parch"]

relatives = titanic.apply(total, axis = 1)
titanic["Relatives"] = relatives

sib = titanic["SibSp"].value_counts().sort_index()
parents = titanic["Parch"].value_counts().sort_index()
total = titanic["Relatives"].value_counts().sort_index()

plt.plot(total.index, total, color = 'blue', marker='.', linewidth = 2, markersize = 7, label = "Total de Parentes")
plt.plot(parents.index, parents, color = 'green', marker='^', linewidth = 2, markersize = 7, label = "Número de irmão/conjuges a bordo")
plt.plot(sib.index, sib, color = 'orange', marker='x', linewidth = 2, markersize = 7, label = "Número de irmão/conjuges a bordo")

plt.xticks([0,1,2,3,4,5,6,7,8,9,10], rotation="horizontal") # Adiciona os "ticks"

plt.xticks(rotation = '45')
plt.legend() # Colocar Legenda, precisa ter LABEL como atributo no PLOT
plt.grid(linestyle = 'dashed')
plt.title("Quantidade de Parentes por Pessoa")

plt.xlabel("Quantidade de Parentes")
plt.ylabel("Quantidade de Pessoas")

plt.show()



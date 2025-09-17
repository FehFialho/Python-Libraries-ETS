import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../pandas/data/respiradores.csv", sep=",")

fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))

eixo[0][0].bar(df.MES, df.TOTAL)
eixo[0][1].bar(df.columns[1:-1], df.sum()[1:-1])
eixo[1][0].scatter(df.MES, df.GOIAS, label = 'Goiás')
eixo[1][1].plot(df.MES, df. PARANA, color = 'purple', marker = 'x', linewidth = 3, markersize = 7)

eixo[0][0].set_title("Gráficos") # TITULO

eixo[0][0].set_ylabel("Teste")

eixo[0][0].tick_params(axis= 'x', labelrotation =45)
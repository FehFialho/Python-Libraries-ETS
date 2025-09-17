import pandas as pd
import matplotlib.pyplot as plt
# Imprimir documentação: help(plt.bar)

resp = pd.read_csv("../Pandas/data/respiradores.csv", sep=",")

# ===== GRÁFICO DE BARRAS VERTICAIS POR MÊS =====
x = resp["MES"] # Jeito 1
y = resp.TOTAL # Jeito 2
# Barra - x | y | Grossura | Align | Cor Dentro | Cor Borda 
plt.bar(x,y, 1.5, align= "center", color = "darkred", edgecolor= "black") 
plt.title("COMPRA DE RESPIRADORES POR MÊS") # Título do Gráfico

plt.xticks(rotation = '45') # Eixo da Legenda X
plt.yticks(rotation = '0') # Eixo da Legenda Y

plt.show()

# >> GRAFICO COM VARIAVEL
total_por_estado = resp.sum()[1:-1]

x = resp.columns[1:-1]
plt.bar(x, total_por_estado, color = "red", zorder = 3) # Barra - x | y | Grossura | Align | Cor Borda
plt.title("COMPRA DE RESPIRADORES POR ESTADO") # Título do Gráfico
plt.xticks(rotation = 'vertical') # Eixo da Legenda X
plt.grid(zorder=0) # Coloca o Grid na ordem 0 (Pensar em Layers)

plt.show()

# ===== GRÁFICO DE BARRAS HORIZONTAIS =====
plt.barh(resp.MES, resp.TOTAL, color = "purple")
plt.title("COMPRA DE RESPIRADORES POR MÊS")

plt.show()

# ===== GRÁFICO DE LINHAS COMPARATIVO ENTRE ESTADOS =====
plt.plot(resp.MES, resp.PARANA, color = 'purple', marker='o', linewidth = 3, markersize = 10, label = "Paraná")
plt.plot(resp.MES, resp['SÃO PAULO'], color = 'blue', marker='o', linewidth = 3, markersize = 10, label = "São Paulo")
# Uma linha por linha.
plt.xticks(rotation = '45')
plt.legend() # Colocar Legenda, precisa ter LABEL como atributo no PLOT
plt.grid(linestyle = 'dashed')
plt.title("COMPRA DE RESPIRADORES POR MÊS NO PARANÁ")
# Configurações Extra


plt.show()
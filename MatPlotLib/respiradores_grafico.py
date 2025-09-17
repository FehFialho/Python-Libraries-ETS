import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../pandas/data/respiradores.csv", sep=",")


# Região Norte
def sumNorte(line):
    return line["AMAZONAS"] + line["ACRE"] + line["RONDONIA"] + line["RORAIMA"] + line["AMAPA"] + line["PARA"] + line["TOCANTINS"]

# Região Nordeste
def sumNordeste(line):
    return line["BAHIA"] + line["SERGIPE"] + line["ALAGOAS"] + line["PERNAMBUCO"] + line["PARAIBA"] + line["RIO GRANDE DO NORTE"] + line["CEARA"] + line["PIAUI"] + line["MARANHÃO"]

# Região Centro-Oeste
def sumCentroOeste(line):
    return line["GOIAS"] + line["MATO GROSSO "] + line["MATO GROSSO DO SUL"] + line["DISTRITO FEDERAL"]

# Região Sudeste
def sumSudeste(line):
    return line["SÃO PAULO"] + line["RIO DE JANEIRO"] + line["ESPIRITO SANTO"] + line["MINAS GERAIS"]

# Região Sul
sul = df["PARANA"] + df["SANTA CATARINA"] + df["RIO GRANDE DO SUL"]

norte = df.apply(sumNorte, axis = 1)
nordeste = df.apply(sumNordeste, axis = 1)
centro_oeste = df.apply(sumCentroOeste, axis = 1)
sudeste = df.apply(sumSudeste, axis = 1)

norte_total = norte.sum()
nordeste_total = nordeste.sum()
centro_oeste_total = centro_oeste.sum()
sudeste_total = sudeste.sum()
sul_total = sul.sum()

regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
valores = [norte_total, nordeste_total, centro_oeste_total, sudeste_total, sul_total]

df["NORTE"] = norte
df["NORDESTE"] = nordeste
df["CENTRO OESTE"] = centro_oeste
df["SUDESTE"] = sudeste
df["SUL"] = sul

mes = df.MES

df = df.loc[:,["SUL","SUDESTE", "CENTRO OESTE", "NORDESTE", "NORTE"]]

x = df.sum()

fig, eixo = plt.subplots(nrows = 1, ncols = 2, figsize = (24,10))
# No erro 'AxesSubplot' usar squeeze = False no fig, eixo

eixo[0].set_title("Valores por Região")
eixo[0].grid(linestyle = 'dashed', zorder = 0)
eixo[0].bar(regioes, valores, zorder = 3, color = 'darkred')

eixo[1].set_title("Valores por Mês")
eixo[1].plot(mes, df.NORTE, color = 'purple', marker='o', linewidth = 3, markersize = 10, label = "Norte")
eixo[1].plot(mes, df.NORDESTE, color = 'blue', marker='o', linewidth = 3, markersize = 10, label = "Nordeste")
eixo[1].plot(mes, df["CENTRO OESTE"], color = 'green', marker='o', linewidth = 3, markersize = 10, label = "Centro Oeste")
eixo[1].plot(mes, df.SUDESTE, color = 'orange', marker='o', linewidth = 3, markersize = 10, label = "Sudeste")
eixo[1].plot(mes, df.SUL, color = 'red', marker='o', linewidth = 3, markersize = 10, label = "Sul")
eixo[1].legend()
eixo[1].grid(linestyle = 'dashed')


# eixo[0][0].plot(df.MES, norte, color = 'darkred', marker = 'o', linewidth = 5, markersize = 1)
# eixo[0][0].set_title("Norte")
# eixo[0][0].tick_params(axis= 'x', labelrotation =45)

# eixo[0][1].plot(df.MES, nordeste, color = 'darkred', marker = 'o', linewidth = 5, markersize = 1)
# eixo[0][1].set_title("Nordeste")
# eixo[0][1].tick_params(axis= 'x', labelrotation =45)

# eixo[0][2].plot(df.MES, centro_oeste, color = 'darkred', marker = 'o', linewidth = 5, markersize = 1)
# eixo[0][2].set_title("Centro Oeste")
# eixo[0][2].tick_params(axis= 'x', labelrotation =45)

# eixo[1][0].plot(df.MES, sudeste, color = 'darkred', marker = 'o', linewidth = 5, markersize = 1)
# eixo[1][0].set_title("Sudeste")
# eixo[1][0].tick_params(axis= 'x', labelrotation =45)

# eixo[1][1].plot(df.MES, sul, color = 'darkred', marker = 'o', linewidth = 5, markersize = 1)
# eixo[1][1].set_title("Sul")
# eixo[1][1].tick_params(axis= 'x', labelrotation =45)
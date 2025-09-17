import pandas as pd

titanic = pd.read_csv("./data/titanic.csv", sep=",")

#Função 
def soma_sibsp_parch(linha):
    return linha["SibSp"] + linha["Parch"]

# Criando nova Coluna
nova_coluna = titanic.apply(soma_sibsp_parch, axis = 1)
# Axis 1 = Soma linha por Linha;
# Axis 2 = Soma coluna por coluna;

titanic["Relatives"] = nova_coluna

# Deletando Colunas
titanic.pop('SibSp')
titanic.pop('Parch')

def search_age_group(line):
    if (line["Age"] < 12):
        return "Kid"
    elif ( (line["Age"] >= 12) & (line["Age"] < 18) ):
        return "Teen"
    elif ( (line["Age"] >= 18) & (line["Age"] < 60) ):
        return "Adult"
    elif (line["Age"] >= 60):
        return "Old"
    else:
        return "Unknown"

ageGroup = titanic.apply(search_age_group, axis = 1)
titanic["Age Group"] = ageGroup
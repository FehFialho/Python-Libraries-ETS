# Arquivo: explicacoes_extras.py

import pandas as pd

# ========================
# EXPLICACOES ADICIONAIS
# ========================

# 1. .loc[:, ["colunas"]]
# Seleciona todas as linhas (:) e colunas específicas
exemplo = pd.read_csv("./data/titanic.csv", sep=",").loc[:, ["Survived", "Pclass"]]
print("Exemplo com .loc:\n", exemplo.head())

# 2. .dropna()
# Remove todas as linhas com valores NaN (nulos)
titanic = pd.read_csv("./data/titanic.csv", sep=",").loc[:, ["Survived","Pclass","Sex", "Age"]]
titanic_sem_nan = titanic.dropna()
print("\nTotal após dropna():", titanic_sem_nan.shape[0])

# 3. .shape
# Retorna uma tupla com (n_linhas, n_colunas)
print("\nShape do DataFrame:", titanic.shape)
print("Número de linhas:", titanic.shape[0])

# 4. .value_counts()
# Conta valores únicos em uma coluna
contagem = titanic["Survived"].value_counts()
print("\nContagem dos valores de Survived:\n", contagem)

# 5. .groupby()
# Agrupa dados por uma coluna e calcula a média
media_idade_por_embarque = titanic.groupby("Embarked")["Age"].mean()
print("\nMédia de idade por ponto de embarque:\n", media_idade_por_embarque)

# 6. .sort_values()
# Ordena valores em ordem crescente
ordenado = titanic.sort_values("Age")
print("\nPrimeiras idades ordenadas:\n", ordenado["Age"].head())

# 6.2 .sort_index()
# Ordena na ordem do index
# Exemplo: Quando usamos o value_counts.

# 7. Operadores lógicos com DataFrame
# Você pode usar condições combinadas com & e |
# Exemplo: passageiros entre 18 e 60 anos
tipo_adulto = titanic[(titanic["Age"] >= 18) & (titanic["Age"] < 60)]
print("\nTotal de adultos:", tipo_adulto.shape[0])

# 8. .describe(include="all")
# Gera estatísticas de todas as colunas, incluindo as categóricas
descricao_completa = titanic.describe(include="all")
print("\nResumo completo:\n", descricao_completa)

# 9. .unique()
# Retorna valores únicos de uma coluna
embarked_unicos = titanic["Embarked"].unique()
print("\nPontos de embarque únicos:", embarked_unicos)

# 10. .fillna(valor)
# Substitui valores NaN por outro valor
media_idade = titanic["Age"].mean()
titanic_preenchido = titanic["Age"].fillna(media_idade)
print("\nExemplo de preenchimento de NaN com média:", titanic_preenchido.head())
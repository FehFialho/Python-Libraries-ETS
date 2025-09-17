import pandas as pd

# Carregando o dataset
titanic = pd.read_csv("./data/titanic.csv", sep=",")

# ========== TRATAMENTO DE DADOS ==========
# Preenchendo valores ausentes em "Age" com a média
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# Criando dataset sem valores ausentes
titanic_sem_na = titanic.dropna()

# ========== FUNÇÃO DE RESUMO ==========
def resumir_colunas_numericas(df):
    for coluna in df.columns:
        if df.dtypes[coluna] == "float64":
            media = df[coluna].mean()
            print(f"A coluna '{coluna}' é numérica. Média: {media:.2f}")

# resumir_colunas_numericas(titanic)

# ========== FILTRAGENS E VISUALIZAÇÕES ==========
# Pessoas com mais de 20 anos
maiores_20 = titanic[titanic["Age"] > 20]

# Todas as colunas menos a última
todas_menos_ultima = titanic[titanic.columns[:-1]]

# ========== DESCRITIVOS ==========
# Descrição geral (numérica)
descricao_geral = titanic.describe()

# Descrição com colunas específicas
descricao_idade_classe = titanic[["Age", "Pclass"]].describe()

# Descrição com colunas categóricas
descricao_completa = titanic.describe(include="all")

# Descrição do dataset sem NaNs
descricao_sem_na = titanic_sem_na.describe()

# ========== ESTATÍSTICAS ESPECÍFICAS ==========
# Valores únicos na coluna "Embarked"
embarked_unicos = titanic["Embarked"].unique()

# Contagem de valores na coluna "Age"
contagem_idades = titanic["Age"].value_counts()

# Média das idades por porto de embarque, arredondada
media_idade_por_embarque = round(titanic.groupby("Embarked")["Age"].mean().sort_values(), 2)

# Valor específico da média de idade para quem embarcou em 'S'
media_s = media_idade_por_embarque.get("S")

# ========== EXTRAS ==========
# Exemplo: verificar se nomes contêm uma palavra
# titanic["Name"].str.contains("Palavra")

# Exemplo: preencher todos os NaNs com zero
# titanic.fillna(0)

# ========== PRINTS (caso queira ver os dados) ==========
print("\n=== Descrição Geral ===\n", descricao_geral)
print("\n=== Valores únicos em 'Embarked':", embarked_unicos)
print("\n=== Média de idade por local de embarque ===\n", media_idade_por_embarque)
print(f"\nMédia de idade de quem embarcou em 'S': {media_s}")

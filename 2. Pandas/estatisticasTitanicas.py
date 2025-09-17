import pandas as pd

titanic = pd.read_csv("./data/titanic.csv", sep=",").loc[:,["Survived","Pclass","Sex", "Age"]]

# Tratamento
#meanAge = titanic["Age"].mean()
#titanic = titanic.fillna(meanAge)
titanic = titanic.dropna()

# Separação
men = titanic[titanic["Sex"] == "male"]
women = titanic[titanic["Sex"] == "female"]
kids = titanic[titanic["Age"] < 12]
teens = titanic[(titanic["Age"] >= 12) & (titanic["Age"] < 18)]
adults = titanic[(titanic["Age"] >= 18) & (titanic["Age"] < 60)]
old = titanic[titanic["Age"] >= 60]

# Porcentagem de Vivos vs Mortos

counts = titanic["Survived"].value_counts()
dead = titanic["Survived"].value_counts().values[0]
dead2 = titanic[titanic["Survived"] == 0]

alive = titanic["Survived"].value_counts().values[1]
alive2 = titanic[titanic["Survived"] == 1]

total = dead + alive
deadPercent = dead/total * 100
alivePercent = alive/total * 100

print(f"\nMortos: {deadPercent:.2f}%")
print(f"Sobreviventes: {alivePercent:.2f}%")

# === VIVOS ===
print("\n============= VIVOS ==============\n")

# Gênero
print("Gênero - Vivos")
print("Homens: ", men[men["Survived"] == 1].shape[0])
print("Mulheres: ", women[women["Survived"] == 1].shape[0])

# Classe - Vivos
print("\nClasse - Vivos")
print("1º Classe Vivos - ", alive2[alive2["Pclass"] == 1].shape[0])
print("2º Classe Vivos - ", alive2[alive2["Pclass"] == 2].shape[0])
print("3º Classe Vivos - ", alive2[alive2["Pclass"] == 3].shape[0])

# 1ª Classe
print("> Homens - ", alive2[(alive2["Pclass"] == 1) & (alive2["Sex"] == "male")].shape[0])
print("> Mulheres - ", alive2[(alive2["Pclass"] == 1) & (alive2["Sex"] == "female")].shape[0])

# Porcentagens
print("\nOutras Porcentagens") 

teste = kids[kids["Survived"] == 1].shape[0]/kids.shape[0]*100

print("Crianças - ", kids[kids["Survived"] == 1].shape[0]/kids.shape[0]*100)
print("Adolescentes - ", teens[teens["Survived"] == 1].shape[0]/teens.shape[0]*100)
print("Adultos - ", adults[adults["Survived"] == 1].shape[0]/adults.shape[0]*100)
print("Idosos - ", old[old["Survived"] == 1].shape[0]/old.shape[0]*100)

# === MORTOS ===
print("\n============= MORTOS ==============\n")

# Gênero
print("Gênero - Mortos")
print("Homens: ", men[men["Survived"] == 0].shape[0])
print("Mulheres: ", women[women["Survived"] == 0].shape[0])

# Classe - Mortos
print("\nClasse - Mortos")
print("1º Classe- ", dead2[dead2["Pclass"] == 1].shape[0])
print("2º Classe - ", dead2[dead2["Pclass"] == 2].shape[0])
print("3º Classe - ", dead2[dead2["Pclass"] == 3].shape[0])

# 3ª Classe
print("> Homens - ", dead2[(dead2["Pclass"] == 3) & (dead2["Sex"] == "male")].shape[0])
print("> Mulheres - ", dead2[(dead2["Pclass"] == 3) & (dead2["Sex"] == "female")].shape[0])


# Botes
print("\n============= BOTES ==============\n")

male_kids = kids[kids["Sex"] == "male"]

boat = women.shape[0] + male_kids.shape[0]

boatPercent = (women[women["Survived"] == 1].shape[0] + male_kids[male_kids["Survived"] == 1].shape[0]) / boat * 100

print("Mulheres e Crianças - ", boat)
print("Mulheres e Crianças - ", boatPercent)




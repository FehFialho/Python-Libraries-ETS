import pandas as pd

cars1 = pd.read_csv("./data/cars93.csv", sep=",").loc[:,["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]]
data = pd.read_csv("./data/bostonhousing.csv", sep=",").loc[:13,["crim", "medv"]]

cars = cars1.dropna()

cars = cars[cars["Passengers"] == 5] 

cars = cars.sort_values(by="MPG.city")

maiorMpg = cars.tail(10)

maisBaratos = maiorMpg.sort_values(by="Price").head(5)

print(data)

new = data[['crim','medv']].head(14)

print(new)
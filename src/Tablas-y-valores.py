import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

test = pd.read_excel("data/test.csv.xlsx")
train = pd.read_excel("data/train.csv.xlsx")

train["Familiares"] = train["SibSp"] + train["Parch"]
test["Familiares"] = test["SibSp"] + test["Parch"]

train["Familiares"].describe() #Esta variable muestra con cuantos familiares viajaba cada pasajero

# Agregar columna 'source' para identificar el origen
train["source"] = "train"
test["source"] = "test"

# Agregar columna Survived a test con valores vacíos
test["Survived"] = np.nan

# Add 'Familiares' column to test before concatenating
test["Familiares"] = test["SibSp"] + test["Parch"]

# Unir verticalmente
combined = pd.concat([train, test], axis=0, ignore_index=True)

print("Tamaño del conjunto combinado:", combined.shape)
(combined.head())
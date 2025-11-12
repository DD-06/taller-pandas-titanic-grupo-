

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde la carpeta del proyecto
test = pd.read_excel("data/test.csv.xlsx")
train = pd.read_excel("data/train.csv.xlsx")

print("Datos de entrenamiento:")
print(train.head())

print("\nDatos de prueba:")
print(test.head())

print("\nInformación del conjunto de prueba:")
print(test.info())

print("\nInformación del conjunto de entrenamiento:")
print(train.info())

print("\nEstadísticas básicas de cada DataFrame:")
print(train.describe())
print(test.describe())

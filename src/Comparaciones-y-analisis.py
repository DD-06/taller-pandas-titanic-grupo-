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
combined.head()

data = combined.copy()
# Verificamos el tamaño de cada conjunto
print("Tamaño de los conjuntos:")
print(data["source"].value_counts())
print("\n" + "-"*60 + "\n")

# Estadísticas generales por conjunto (train y test)
print("Estadísticas descriptivas por conjunto (numéricas):")
print(data.groupby("source").describe())

print("\n" + "-"*60 + "\n")

# Comparamos la proporción de hombres y mujeres en cada conjunto
print("Distribución de sexo por conjunto:")
print(data.groupby("source")["Sex"].value_counts(normalize=True))

print("\n" + "-"*60 + "\n")

# Comparamos clases de boleto (Pclass) en cada conjunto
print("Distribución de clases por conjunto:")
print(data.groupby("source")["Pclass"].value_counts(normalize=True))

print("\n" + "-"*60 + "\n")

# Comparamos edad promedio
print("Edad promedio por conjunto:")
print(data.groupby("source")["Age"].mean())

print("\n" + "-"*60 + "\n")

# Comparamos tarifas promedio
print("Tarifa promedio (Fare) por conjunto:")
print(data.groupby("source")["Fare"].mean())

#Se muestran las columnas con valores faltantes (NaN), como Age, Cabin, Embarked o Fare.
faltantes = combined.isnull().sum()
print("Valores faltantes por columna:")
print(faltantes[faltantes > 0])

# a) Edad promedio
print("Edad promedio:", train["Age"].mean())

# b) Sobrevivientes y fallecidos
print(train["Survived"].value_counts())

# c) Tarifa promedio en primera clase
print("Tarifa promedio 1ra clase:", train.loc[train["Pclass"] == 1, "Fare"].mean())

# e) Edad más joven y más vieja
print("Edad mínima:", train["Age"].min(), " | Edad máxima:", train["Age"].max())

# f) Pasajeros por puerto
print(train["Embarked"].value_counts())

combined["Familiares"] = combined["SibSp"] + combined["Parch"]

# Pasajeros con al menos 1 familiar
con_familia = combined[combined["Familiares"] > 0]
print("número de pasajeros con familiares a bordo:", con_familia.shape[0])

# Crear una nueva columna indicadora
combined["viajo_solo"] = combined["Familiares"] == 0

# Contar proporciones y totales
print("\nConteo de pasajeros que viajaron solos vs con familia:")
print(combined["viajo_solo"].value_counts())

print("\nProporciones:")
print(combined["viajo_solo"].value_counts(normalize=True))

# Crear la nueva variable "Familiares" sumando SibSp y Parch
combined["Familiares"] = combined["SibSp"] + combined["Parch"]

# Crear la columna "GrupoFamilia" según el número de familiares
grupo = []
for i in combined["Familiares"]:
    if i == 0:
        grupo.append("Grupo 1: sin familiares")
    elif i >= 1 and i <= 3:
        grupo.append("Grupo 2: familias pequeñas")
    else:
        grupo.append("Grupo 3: familias grandes")

combined["GrupoFamilia"] = grupo

# Crear columna que diga si la persona tenía cabina o no
combined["TieneCabina"] = combined["Cabin"].notna()

# Contar cuántas personas hay en cada grupo familiar
conteo = combined.groupby("GrupoFamilia")["TieneCabina"].value_counts()

print("Distribución de cabinas por grupo familiar:\n")
print(conteo)

# También ver cuántas personas totales hay en cada grupo
print("\nCantidad total por grupo familiar:\n")
print(combined["GrupoFamilia"].value_counts())

datos = combined.copy()
#Copiar el DataFrame combinado
grupo_edad = []
#Separacion de los grupos basandose en la edad
for e in datos["Age"]:
    if pd.isna(e):
        grupo_edad.append("N.R")
    elif e <= 10:
        grupo_edad.append("Niño")
    elif e >= 18 and e <= 50:
        grupo_edad.append("Adulto")
    elif e > 50:
        grupo_edad.append("Mayor")
    else: 
        grupo_edad.append("Adolecente")
#Asignar columna de "Grupo etario"
datos["grupo_etario"] = grupo_edad
#Crear columna para comprobar si tienen columna o no 
datos["Tiene_cabina"] = datos["Cabin"].notna()
#Ver cuántas personas sobrevivieron o no, por grupo etario, sexo y cabina
tabla = datos.groupby(["grupo_etario", "Sex", "TieneCabina"])["Survived"].value_counts()

print("\nDistribución de supervivencia por grupo etario, sexo y cabina:\n")
print(tabla)

tasa = datos.groupby(["grupo_etario", "Sex", "TieneCabina"])["Survived"].mean()

print("\nTasa (proporción) de supervivencia en cada grupo:\n")
print(tasa)
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#Carga del dataframe combinado
combined = pd.read_excel("data/datos_combinados.xlsx")

datos = combined.copy() #Se hace una copia de la base combinada y se nombra como datos 

# Usamos solo los datos con información de supervivencia
DataFrame = datos[datos['Survived'].notna()]

# Histograma de edades
plt.figure(figsize=(8,5))
plt.hist(DataFrame["Age"].dropna(), bins=20, color="#3498db", edgecolor="black")
plt.title("Distribución de edades de los pasajeros")
plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")
plt.show()
# La mayoría de los pasajeros tenían entre 20 y 40 años.

# Histograma de tarifas
plt.figure(figsize=(8,5))
plt.hist(DataFrame["Fare"].dropna(), bins=25, color="#9b59b6", edgecolor="black")
plt.title("Distribución de tarifas pagadas")
plt.xlabel("Tarifa ($)")
plt.ylabel("Cantidad de pasajeros")
plt.show()
# La mayoría de las tarifas fueron bajas, típicas de pasajeros de tercera clase.

# Gráfico de barras: promedio de edad según supervivencia
plt.figure(figsize=(7,5))
edades = DataFrame.groupby("Survived")["Age"].mean()
plt.bar(["No sobrevivió", "Sobrevivió"], edades, color=["#e74c3c", "#2ecc71"], edgecolor="black")
plt.title("Edad promedio según supervivencia")
plt.xlabel("Supervivencia")
plt.ylabel("Edad promedio")
plt.show()
# Los sobrevivientes eran un poco más jóvenes en promedio.

# Gráfico de barras: cantidad por sexo
plt.figure(figsize=(7,5))
sexos = DataFrame["Sex"].value_counts()
plt.bar(sexos.index, sexos.values, color=["#3498db", "#e67e22"], edgecolor="black")
plt.title("Distribución de pasajeros por sexo")
plt.xlabel("Sexo")
plt.ylabel("Cantidad de pasajeros")
plt.show()
# Había más hombres que mujeres a bordo.

# Gráfico de barras: porcentaje de supervivencia por sexo
plt.figure(figsize=(7,5))
tasa_sexo = DataFrame.groupby("Sex")["Survived"].mean()
plt.bar(tasa_sexo.index, tasa_sexo.values, color=["#e74c3c", "#2ecc71"], edgecolor="black")
plt.title("Porcentaje de supervivencia por sexo")
plt.xlabel("Sexo")
plt.ylabel("Proporción de sobrevivientes")
plt.show()
# Las mujeres tuvieron una tasa de supervivencia más alta.
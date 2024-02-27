import matplotlib.pyplot as plt
import pandas as pd


iris_data = pd.read_csv('iris.csv')


plt.figure(figsize=(15, 10))
for species, group in iris_data.groupby('species'):
    plt.scatter(group['sepal.length'], group['sepal.width'], label=species)

# Füge Titel und Beschriftungen hinzu
plt.title('Streudiagramm der Iris-Daten')
plt.xlabel('Sepalenlänge (cm)')
plt.ylabel('Sepalenbreite (cm)')
plt.legend()

# Zeige das Diagramm an
plt.show()
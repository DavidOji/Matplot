import pandas as pd

# Aufgabe 1
df = pd.read_csv('iris.csv')
print(df.head())
print(df.tail())
print(df.info())
print("#"*50)

# Aufgabe 2
# 1. Spalten auswählen
selected_columns = df[['sepal.length', 'sepal.width']]
print("\nErste 10 Zeilen der ausgewählten Spalten:")
print(selected_columns.head(10))

# 2. Bedingte Auswahl für 'setosa'
setosa = df[df['species'] == 'Setosa']
print("\nZeilen, bei denen die species 'Setosa' ist:")
print(setosa)

# 3. Mehrere Bedingungen für 'versicolor' und petal_length > 1.5
versicolor_cond = (df['species'] == 'Versicolor') & (df['petal.length'] > 1.5)
versicolor_filtered = df[versicolor_cond]
print("\nZeilen, bei denen die species 'Versicolor' ist und petal_length > 1.5:")
print(versicolor_filtered)

#Aufgabe 3
# 1. Neue Spalte hinzufügen: Fläche des Sepal berechnen
df['sepal_area'] = df['sepal.length'] * df['sepal.width']

# 2. Werte in der species-Spalte ändern
df['species'] = df['species'].replace({'Setosa': 'S', 'Versicolor': 'Ve', 'Virginica': 'Vi'})

# 3. Zeilen löschen: Alle Zeilen, in denen sepal_length < 4.5 ist, entfernen
df = df[df['sepal.length'] >= 4.5]

# Ergebnisse anzeigen
print("\n1. Neue Spalte 'sepal_area' hinzugefügt:")
print(df.head())

print("\n2. Werte in der 'species'-Spalte geändert:")
print(df['species'].unique())

print("\n3. Zeilen, in denen sepal_length < 4.5 ist, entfernt:")
print(df.head())


# Aufgabe 4

# 1. Deskriptive Statistiken anzeigen
descriptive_stats = df.describe()
print("\n1. Deskriptive Statistiken:")
print(descriptive_stats)

# 2. Gruppieren und Aggregieren: Durchschnitt von sepal_length nach species
avg_sepal_length_by_species = df.groupby('species')['sepal.length'].mean()
print("\n2. Durchschnittliche sepal_length, gruppiert nach species:")
print(avg_sepal_length_by_species)

# 3. Einzigartige Werte in der species-Spalte finden
unique_species_values = df['species'].unique()
print("\n3. Einzigartige Werte in der 'species'-Spalte:")
print(unique_species_values)


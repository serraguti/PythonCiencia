import pandas as pd

print("Lectura de CSV")

#ALMACENAMOS LOS DATOS DEL CSV DENTRO DE UN DATAFRAME
df = pd.read_csv('data/datos.csv', delimiter=';')
print(df)
#PRIMERAS 5 FILAS
print(df.head())
df_sorted = df.sort_values('edad')
print(df_sorted)

#Podemos recuperar datos estadísticos como puede ser la Media de edad
media_edad = df['edad'].mean()
print(f"Media de edad: {media_edad}")

#PODEMOS AGRUPAR POR COLUMNAS Y RECUPERAR DATOS
df_grupo = df.groupby('ocupacion').size()
print(df_grupo)


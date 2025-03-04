import pandas as pd

print("Primer ejemplo DataFrame")

#Vamos a crear un diccionario con elementos que se llaman SERIES
#No deja de ser un diccionario con valores que van correspondientes entre 
#ellos, aunque podrían no ser correspondientes.
datos = {
    'nombres': ['Lucía', 'Andrea', 'Alex', "Antonia"]
    , 'edad': [22, 17, 48, 70]   
    , 'ciudad': ['Segovia', 'Parla', 'Madrid', 'Toledo']  
         }
#ALMACENAMOS LOS DATOS EN UN DATAFRAME
df = pd.DataFrame(datos)
print(df)

#PODEMOS FILTRAR LOS DATOS DE UN DATAFRAME
#LA FORMA DE FILTRAR ES MEDIANTE LA SIGUIENTE SINTAXIS:
# df[ df[COLUMNA] == valor ]
print("--------Dataframe filtrado--------")
df_filtrado = df[df['edad']>30]
print(df_filtrado)

print("--------Dataframe ordenado--------")
#ORDENAR POR UNA O VARIAS COLUMNAS: df.sort_values(COLUMNA)
df_sorted = df.sort_values('edad')
print(df_sorted) 
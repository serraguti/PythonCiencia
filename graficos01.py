import matplotlib.pyplot as plt

#LA MAYORIA DE LOS GRAFICOS SUELEN TENER DOS EJES DE COORDENADAS
#PARA REPRESENTAR SUS DATOS (x, y)
x = ['Betis', 'Atletico de Madrid', 'Barcelona', 'Real Madrid']
#VALOR DE MERCADO
y = [5, 10, 15, 20]

#CREAMOS EL GRAFICO MEDIANTE plt Y CON UN METODO IREMOS INDICANDO
#EL TIPO DE GRAFICO QUE QUEREMOS
#BARRAS
plt.bar(x, y)
#PERSONALIZAR EL GRAFICO
plt.title("Gráfico de barras")
plt.xlabel("Equipos")
plt.ylabel("Valor de mercado")
#PODEMOS ALMACENAR EL GRAFICO EN UNA IMAGEN
plt.savefig('images/barras.png')
plt.show()
import matplotlib.pyplot as plt

#LA MAYORIA DE LOS GRAFICOS SUELEN TENER DOS EJES DE COORDENADAS
#PARA REPRESENTAR SUS DATOS (x, y)
x = ['Betis', 'Atletico de Madrid', 'Barcelona', 'Real Madrid']
#VALOR DE MERCADO
y = [5, 2, 15, 20]

#LINEAL
plt.plot(x, y)
#PERSONALIZAR EL GRAFICO
plt.title("Gráfico de líneas")
plt.xlabel("Equipos")
plt.ylabel("Valor de mercado")
#PODEMOS ALMACENAR EL GRAFICO EN UNA IMAGEN
plt.savefig('images/lineal.png')
plt.show()
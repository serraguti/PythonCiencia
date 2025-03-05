import matplotlib.pyplot as plt

etiquetas = ['Betis', 'Atletico de Madrid', 'Barcelona', 'Real Madrid']
#VALOR DE MERCADO
valores = [5, 2, 15, 20]

plt.pie(valores, labels=etiquetas)
plt.title("Gráfico de Tarta")
plt.savefig('images/circular.png')
plt.show()
import matplotlib.pyplot as plt

#CREAMOS UNA LISTA/TUPLA
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
temperaturas = []

#REALIZAMOS UN BUCLE PARA RELLENAR LOS DATOS
for i in range(len(semana)):
    print(f"Introduzca temperatura para {semana[i]}")
    temp = int(input())
    temperaturas.append(temp)

plt.plot(semana, temperaturas, label="Semana 1")
#PODEMOS INCLUIR MAS DATOS DENTRO DEL GRAFICO LINEAL 
#SIEMPRE QUE PONGAMOS UNA LABEL A CADA plot()
temperaturas2 = [5, 20, 8, 12, 19, 22, 30]
plt.plot(semana, temperaturas2, label="Semana 2")
plt.legend()
plt.title("Temperaturas semanales")
plt.xlabel("Día semana")
plt.ylabel("Temperatura")
plt.show()
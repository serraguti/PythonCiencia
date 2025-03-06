import matplotlib.pyplot as plt

#CREAMOS UNA LISTA/TUPLA
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
temperaturas = []

#REALIZAMOS UN BUCLE PARA RELLENAR LOS DATOS
for i in range(len(semana)):
    print(f"Introduzca temperatura para {semana[i]}")
    temp = int(input())
    temperaturas.append(temp)

plt.plot(semana, temperaturas)
plt.title("Temperaturas semana 1 de marzo")
plt.xlabel("Día semana")
plt.ylabel("Temperatura")
plt.show()
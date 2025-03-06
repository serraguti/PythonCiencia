import oracledb
import matplotlib.pyplot as plt

print("Gráficos con BBDD")
connection = oracledb.connect(user='SYSTEM'
                              , password='oracle', dsn='localhost/xe')
sql = """
select OFICIO, AVG(SALARIO) as MEDIA from EMP 
group by OFICIO
"""
oficios = []
medias = []
cursor = connection.cursor()
cursor.execute(sql)
for row in cursor:
    oficios.append(row[0])
    medias.append(row[1])
cursor.close()
connection.close()
plt.pie(medias, labels=oficios)
plt.title("Gráfico media salarial EMP")
plt.show()

import oracledb
import matplotlib.pyplot as plt

print("Gráfico de Doctores por Hospital")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
hospitales = []
personas = []
cursor = connection.cursor()
sql = """
select count(DOCTOR.DOCTOR_NO) as PERSONAS
, HOSPITAL.NOMBRE
from DOCTOR
inner join HOSPITAL
on DOCTOR.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD
group by HOSPITAL.NOMBRE
"""
cursor.execute(sql)
for numero, nombre in cursor:
    hospitales.append(nombre)
    personas.append(numero)
cursor.close()
connection.close()
plt.pie(personas, labels=hospitales)
plt.title("Doctores por hospital")
plt.show()
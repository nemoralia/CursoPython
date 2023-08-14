import random
import numpy as np

#Crear datos aleatorios
sexo = ["MASCULINO","FEMENINO","NO ESPECIFICA"]
sexo_aleatorio = random.choice(sexo)
print("SEXO: ", sexo_aleatorio)

edad_aleatorio = random.randint(28 , 60)
print("EDAD: ",edad_aleatorio)

altura_aleatorio = random.uniform(165.0 , 210.0)
print("ALTURA: ",round(altura_aleatorio,1))

peso_aleatorio = random.randint(50, 110)
print("PESO: ",peso_aleatorio)

horas_descanso = random.uniform(0.0, 10.0)
print("HORAS DESCANSO: ",round(horas_descanso,1))

horas_trabajo = random.uniform(0.0, 10.0)
print("HORAS TRABAJO/ESTUDIO: ",round(horas_trabajo,1))

horas_ejercicio = random.uniform(0.0, 4.0)
print("HORAS EJERCICIO: ",round(horas_ejercicio,1))

#Creación de matriz
datosaleatorios1=[
['SEXO','EDAD','ALTURA','PESO','HS DESCANSO','HS TRABAJO/ESTUDIO','HS EJERCICIO'],
[sexo_aleatorio,edad_aleatorio,altura_aleatorio,peso_aleatorio,horas_descanso,horas_trabajo,horas_ejercicio]]

datosaleatorios=np.array(datosaleatorios1)
print(datosaleatorios)


#Encontrar la media en los datos de altura, peso, y horas de descanso, trabajo y ejercicios

#media altura
mediaaltura = np.mean(altura_aleatorio)
print("MEDIA ALTURA: ",mediaaltura)

#media peso
mediapeso = np.mean(peso_aleatorio)
print("MEDIA PESO: ",mediapeso)

#media descanso
mediadescanso = np.mean(horas_descanso)
print("MEDIA HS DESCANSO: ",mediadescanso)

#media trabajo
mediatrabajo = np.mean(horas_trabajo)
print("MEDIA HS TRABAJO: ",mediatrabajo)

#media ejercicio
mediaejercicio = np.mean(horas_ejercicio)
print("MEDIA HS EJERCICIO: ",mediaejercicio)


#graficar peso y altura
import matplotlib.pyplot as plt

np.random.seed(10)
peso_aleatorio = np.random.normal(loc=50, scale=15, size=100)

plt.figure(figsize=(8, 6))
plt.hist(peso_aleatorio, bins=3, edgecolor='black', alpha=0.7)
plt.axvline(mediapeso, color='red', linestyle='dashed', linewidth=2, label='Media (peso)')
plt.xlabel('Peso')
plt.ylabel('Frecuencia')
plt.title('Histograma de Peso')
plt.legend()
plt.show()

np.random.seed(10)
altura_aleatorio = np.random.normal(loc=50, scale=15, size=100)

plt.figure(figsize=(8, 6))
plt.hist(altura_aleatorio, bins=3, edgecolor='black', alpha=0.7)
plt.axvline(mediaaltura, color='red', linestyle='dashed', linewidth=2, label='Media (altura)')
plt.xlabel('Altura')
plt.ylabel('Frecuencia')
plt.title('Histograma de Altura')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import time


# Configura el lienzo para trazar los puntos 
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

m = 0
c = 1

# Usamos (x-a)^2 + (y-b)^2 = r^2 para iterar 100 veces en valores entre el 0 y 2pi
#Tambien iniciamos el tiempo y lo terminamos antes de iterar el circulo

start_time =  time.time()
cx, cy, r = 2, 2, 4
for angle in np.linspace(0, 2*np.pi, 100):
    x = cx + r * np.cos(angle)
    y = cy + r * np.sin(angle)
    ax.plot(x, y, 'bo', markersize=1.5)

end_time = time.time()
elapsed_time2 = end_time - start_time
print("tiempo: ", elapsed_time2,  "del circulo ")

# Usamos (x/a)^2 + (y/b)^2 = 1 para iterar 100 veces en los mismos puntos del circulo
start_time =  time.time()


a, b = 13, 6
for angle in np.linspace(0, 2*np.pi, 100):
    x = cx + a * np.cos(angle)
    y = cy + b * np.sin(angle)
    ax.plot(x, y, 'go', markersize=2)

end_time = time.time()
elapsed_time3 = end_time - start_time
print("tiempo: ", elapsed_time3,  "de la elipse")


# La ecuacion (x/a)^2 - (y/b)^2 = 1 la vamos a iterar de forma doble para crear los dos lados del hiperbole esta 
# esta solo será con 50 iteraciones y antes de esó empieza a contar el tiempo en que lo hace
star_time = time.time()

a, b = 2, 4
for x in np.linspace(-10, -a, 50):
    y = b * np.sqrt((x**2 / a**2) - 1)
    ax.plot(x, y, 'ro', markersize=1)
    ax.plot(x, -y, 'ro', markersize=1)
for x in np.linspace(a, 10, 50):
    y = b * np.sqrt((x**2 / a**2) - 1)
    ax.plot(x, y, 'ro', markersize=1)
    ax.plot(x, -y, 'ro', markersize=1)

end_time = time.time()
elapsed_time4 = end_time - star_time
print("Tiempo: ", elapsed_time4, "del hiperbole")

#El for para 30 iteraciones de una linea entre el parametro -5 y 5
star_time = time.time()

for x in np.linspace(-5, 5, 30):
    y = m * x + c
    ax.plot(x, y, 'ro', markersize=1)

end_time = time.time()
elapsed_time5 = end_time - star_time
print("Tiempo: ", elapsed_time5, "de la linea recta")
# Mostrar todo
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import time


def eficienciaDeAlgoritmos():
    
#Inicio del tiempo del circulo
    start_time =  time.time()

    r = 6.9
    Angle = np.linspace(0, 2 * np.pi, 30)
    x = r * np.cos(Angle)
    y = r * np.sin(Angle)

    plt.figure()
    plt.plot(x, y, label=f'Radio {r}', color='Blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Círculo')
    plt.legend()
    plt.grid(True)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("tiempo: ", elapsed_time,  "del circulo ")

#Inicio del tiempo de la elipse
    start_time =  time.time()
    a, b = 2, 8.5
    theta = np.linspace(0, 2 * np.pi, 400)
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    plt.figure()
    plt.plot(x, y, label=f'Elipse {a} y {b}', color='Blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Elipse')
    plt.legend()
    plt.grid(True)

    end_time = time.time()
    elapsed_time2 = end_time - start_time
    print("tiempo: ", elapsed_time2,  "del Elipse ")

#Inicio del tiempo de la linea
    start_time =  time.time()

    m, b = 0, 2
    x = np.linspace(-0, 7.5, 400)
    y = m * x + b

    plt.figure()
    plt.plot(x, y, label=f'y = {m}x + {b}', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Línea')
    plt.legend()
    plt.grid(True)

    end_time = time.time()
    elapsed_time3 = end_time - start_time
    print("tiempo: ", elapsed_time3,  "de la linea ")

# Inicio del tiempo de la hipérbola
    start_time = time.time()

    a, b = 6.5, 6.8
    x1 = np.linspace(-7.5, -a, 200)
    x2 = np.linspace(a, 7.5, 200)
    
    y1 = b * np.sqrt((x1**2 / a**2) - 1)
    y2 = b * np.sqrt((x2**2 / a**2) - 1)

    plt.figure()
    plt.plot(x1, y1, 'b', label=f'Hipérbola {a} y {b}')
    plt.plot(x1, -y1, 'b')
    plt.plot(x2, y2, 'b')
    plt.plot(x2, -y2, 'b')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hipérbola')
    plt.legend()
    plt.grid(True)

    end_time = time.time()
    elapsed_time4 = end_time - start_time
    print("tiempo: ", elapsed_time4,  "de la hiperbola ")

    plt.show()

eficienciaDeAlgoritmos()

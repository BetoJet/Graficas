import matplotlib.pyplot as plt


#Funcion con 4 parametros 
def Brasehnman(x1, y1, x2, y2):
    puntitos = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

#Un while para que sepa cuando llegó al final y como ajustar el error 
    while True:
        puntitos.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return puntitos


#Puntos iniciales de las lineas
x1, y1 = 2, 3
x2, y2 = 14, 8
puntitos = Brasehnman(x1, y1, x2, y2)

#Graficadora de matplotlib y los limites en x, y
x_vals, y_vals = zip(*puntitos)
plt.plot(x_vals, y_vals, marker='1', color='red', linestyle='none')
plt.grid(True)
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Línea con Algoritmo de Bresenham")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Definir los parámetros del elipse
semieje_x = 2
semieje_y = 1
centro = (0, 0)
angulo_rotacion = 30  # En grados

# Crear un conjunto de puntos para el elipse
theta = np.linspace(0, 2*np.pi, 100)
x = semieje_x * np.cos(theta)
y = semieje_y * np.sin(theta)

# Rotar el elipse
rotacion_matrix = np.array([[np.cos(np.radians(angulo_rotacion)), -np.sin(np.radians(angulo_rotacion))],
                            [np.sin(np.radians(angulo_rotacion)), np.cos(np.radians(angulo_rotacion))]])
rotated_points = np.dot(rotacion_matrix, np.array([x, y]))

# Trasladar el elipse al centro especificado
x_rotated, y_rotated = rotated_points[0] + centro[0], rotated_points[1] + centro[1]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar el elipse
ax.plot(x_rotated, y_rotated, label='Elipse')

# Configurar aspecto de la gráfica
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Elipse')

# Mostrar la leyenda
ax.legend()

# Mostrar la gráfica
plt.show()

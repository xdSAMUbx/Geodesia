import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del elipsoide
a, b, c = 2, 3, 4

# Crear una malla tridimensional
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

# Coordenadas cartesianas del elipsoide
x = a * np.sin(phi) * np.cos(theta)
y = b * np.sin(phi) * np.sin(theta)
z = c * np.cos(phi)

# Crear la figura tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el elipsoide
ax.plot_surface(x, y, z, color='b', alpha=0.6)

# Configuraciones adicionales para la visualización
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Elipsoide tridimensional')

# Mostrar la figura interactiva
plt.show()
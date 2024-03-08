import matplotlib.pyplot as plt

# Datos proporcionados
precio = [4, 5, 6, 7, 8, 9]
cantidad_demandada = [135, 104, 81, 68, 53, 39]
cantidad_ofrecida = [26, 53, 81, 98, 110, 121]

# Crear el gráfico de dispersión
plt.scatter(cantidad_demandada, precio, label='Cantidad Demandada', color='blue')
plt.scatter(cantidad_ofrecida, precio, label='Cantidad Ofrecida', color='red')

# Unir los puntos con líneas
plt.plot(cantidad_demandada, precio, linestyle='-', marker='o', color='blue')
plt.plot(cantidad_ofrecida, precio, linestyle='-', marker='o', color='red')

# Encontrar el índice del punto de equilibrio (donde se cruzan las curvas)
indice_equilibrio = next(i for i, (x, y) in enumerate(zip(cantidad_demandada, cantidad_ofrecida)) if x == y)

# Unir los puntos con líneas hasta el punto de equilibrio
plt.plot(cantidad_demandada[:indice_equilibrio+1], precio[:indice_equilibrio+1], linestyle='-', marker='o', color='blue')
plt.plot(cantidad_ofrecida[:indice_equilibrio+1], precio[:indice_equilibrio+1], linestyle='-', marker='o', color='red')

# Mostrar el punto de equilibrio con una etiqueta
plt.scatter(cantidad_demandada[indice_equilibrio], precio[indice_equilibrio], color='green', marker='X', s=100, label='Punto de Equilibrio')
plt.text(cantidad_demandada[indice_equilibrio] + 5, precio[indice_equilibrio] - 0.5, f'({cantidad_demandada[indice_equilibrio]}, {precio[indice_equilibrio]})', color='green')

# Configurar el gráfico
plt.title('Mercado De Pizzas')
plt.xlabel('Cantidad de Pizzas')
plt.ylabel('Precio de Pizzas')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

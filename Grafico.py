import matplotlib.pyplot as plt


n_values = [1, 5, 10, 15, 20]
rec_time = [0.00001, 0.0001, 0.001, 0.01, 0.05]
iter_time = [0.00001, 0.00005, 0.0003, 0.001, 0.005]

plt.plot(n_values, rec_time, label='Recursivo')
plt.plot(n_values, iter_time, label='Iterativo')
plt.xlabel('n')
plt.ylabel('Tiempo (s)')
plt.title('Comparación de tiempos de factorial')
plt.legend()
plt.show()

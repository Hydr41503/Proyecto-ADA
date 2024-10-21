import matplotlib.pyplot as plt

# Datos de ejecución de Quick Sort para Java, Python y C++
data_java = {
    "100": 7.13E-5, "500": 3.6E-5, "1000": 8.593E-4, "2000": 9.6E-5, "3000": 1.445E-4,
    "4000": 2.551E-4, "5000": 3.49E-4, "6000": 4.15E-4, "7000": 5.041E-4, "8000": 6.084E-4,
    "9000": 6.065E-4, "10000": 0.0045415, "20000": 0.0028142, "30000": 0.0039751, "40000": 0.0075489,
    "50000": 0.0107377, "60000": 0.0147837, "70000": 0.0189462, "80000": 0.0208368, "90000": 0.0254078,
    "100000": 0.0298444
}

data_python = {
    "100": 0.000395, "500": 0.000436, "1000": 0.003041, "2000": 0.001477, "3000": 0.001952,
    "4000": 0.002679, "5000": 0.003465, "6000": 0.004118, "7000": 0.009014, "8000": 0.007722,
    "9000": 0.005784, "10000": 0.025202, "20000": 0.012908, "30000": 0.019269, "40000": 0.029569,
    "50000": 0.035701, "60000": 0.055505, "70000": 0.136349, "80000": 0.056891, "90000": 0.072493,
    "100000": 0.064060
}

data_cpp = {
    "100": 0.0, "500": 0.000997, "1000": 0.0, "2000": 0.0, "3000": 0.001404,
    "4000": 0.001036, "5000": 0.000785, "6000": 0.001345, "7000": 0.000996, "8000": 0.000997,
    "9000": 0.001032, "10000": 0.004732, "20000": 0.011968, "30000": 0.035901, "40000": 0.063831,
    "50000": 0.042460, "60000": 0.114394, "70000": 0.147599, "80000": 0.175996, "90000": 0.140376,
    "100000": 0.216257
}

# Convertir tamaños de archivos a enteros
file_sizes = sorted([int(size) for size in data_java.keys()])

# Crear listas de tiempos correspondientes a cada lenguaje
times_java = [data_java[str(size)] for size in file_sizes]
times_python = [data_python[str(size)] for size in file_sizes]
times_cpp = [data_cpp[str(size)] for size in file_sizes]

# Graficar los tiempos
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, times_java, marker='o', label='Java')
plt.plot(file_sizes, times_python, marker='o', label='Python')
plt.plot(file_sizes, times_cpp, marker='o', label='C++')

# Etiquetas y título
plt.xlabel('Tamaño del archivo (número de datos)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de Quick Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

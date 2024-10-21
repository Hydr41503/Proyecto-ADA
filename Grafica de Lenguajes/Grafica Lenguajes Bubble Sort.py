import matplotlib.pyplot as plt

# Datos de ejecución de Bubble Sort para Java, Python y C++
data_java = {
    "100": 0.000226, "500": 0.0002446, "1000": 0.0139755, "2000": 0.0038905, "3000": 0.0081268,
    "4000": 0.0141797, "5000": 0.0212786, "6000": 0.0313519, "7000": 0.0455943, "8000": 0.0587551,
    "9000": 0.078018, "10000": 0.1185941, "20000": 0.4897557, "30000": 1.0882285, "40000": 1.9034129,
    "50000": 2.9981747, "60000": 4.3178004, "70000": 5.916058, "80000": 8.207815, "90000": 9.6708755,
    "100000": 16.0731417
}

data_python = {
    "100": 0.000351, "500": 0.007967, "1000": 0.042623, "2000": 0.155590, "3000": 0.358630,
    "4000": 0.645569, "5000": 1.022876, "6000": 1.481326, "7000": 2.020379, "8000": 2.659690,
    "9000": 3.361499, "10000": 4.432389, "20000": 16.823748, "30000": 38.325071, "40000": 67.763661,
    "50000": 107.131926, "60000": 153.047824, "70000": 209.673083, "80000": 271.074176,
    "90000": 345.050077, "100000": 422.016129
}

data_cpp = {
    "100": 0.0, "500": 0.004073, "1000": 0.012377, "2000": 0.068767, "3000": 0.156408,
    "4000": 0.273753, "5000": 0.426600, "6000": 0.618661, "7000": 0.858208, "8000": 1.112569,
    "9000": 0.799246, "10000": 1.154201, "20000": 6.796895, "30000": 15.405760, "40000": 27.616360,
    "50000": 43.862309, "60000": 63.530091, "70000": 84.352952, "80000": 87.254917, "90000": 69.975658,
    "100000": 104.283769
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
plt.title('Comparación de tiempos de Bubble Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

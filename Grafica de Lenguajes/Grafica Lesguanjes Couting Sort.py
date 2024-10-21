import matplotlib.pyplot as plt

# Datos de ejecución de Counting Sort para Java, Python y C++
data_java = {
    "100": 0.0039566, "500": 0.0002935, "1000": 0.0006415, "2000": 0.000174, "3000": 0.0002657, 
    "4000": 0.0018748, "5000": 0.0009076, "6000": 0.0008539, "7000": 0.0011925, "8000": 0.0010385,
    "9000": 0.0011117, "10000": 0.0034233, "20000": 0.0010622, "30000": 0.0014065, "40000": 0.0120719,
    "50000": 0.0095115, "60000": 0.0105185, "70000": 0.0071263, "80000": 0.0068546, "90000": 0.0079123,
    "100000": 0.0105148
}

data_python = {
    "100": 0.000105, "500": 0.000610, "1000": 0.000762, "2000": 0.001848, "3000": 0.003541, 
    "4000": 0.003561, "5000": 0.004329, "6000": 0.001608, "7000": 0.001775, "8000": 0.002140,
    "9000": 0.002264, "10000": 0.007242, "20000": 0.018721, "30000": 0.028016, "40000": 0.038496,
    "50000": 0.013249, "60000": 0.015904, "70000": 0.017725, "80000": 0.020897, "90000": 0.025393,
    "100000": 0.025593
}

data_cpp = {
    "100": 0.0, "500": 0.000062, "1000": 0.0, "2000": 0.0, "3000": 0.0, 
    "4000": 0.0, "5000": 0.000980, "6000": 0.0, "7000": 0.0, "8000": 0.0,
    "9000": 0.000998, "10000": 0.000839, "20000": 0.002991, "30000": 0.003989, "40000": 0.006030,
    "50000": 0.004980, "60000": 0.002992, "70000": 0.004533, "80000": 0.004092, "90000": 0.005984,
    "100000": 0.012021
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
plt.title('Comparación de tiempos de Counting Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

import matplotlib.pyplot as plt

# Datos de ejecución de Heap Sort para Java, Python y C++
data_java = {
    "100": 1.972E-4, "500": 4.32E-5, "1000": 4.552E-4, "2000": 1.861E-4, "3000": 2.786E-4, 
    "4000": 5.374E-4, "5000": 5.047E-4, "6000": 8.409E-4, "7000": 0.0011571, "8000": 9.282E-4,
    "9000": 9.617E-4, "10000": 0.0053684, "20000": 0.0028579, "30000": 0.0031534, "40000": 0.0060884,
    "50000": 0.0060455, "60000": 0.0071117, "70000": 0.0085283, "80000": 0.0104696, "90000": 0.0095672,
    "100000": 0.0118272
}

data_python = {
    "100": 0.000607, "500": 0.001032, "1000": 0.007915, "2000": 0.005431, "3000": 0.008478, 
    "4000": 0.011686, "5000": 0.015396, "6000": 0.018462, "7000": 0.032314, "8000": 0.025447,
    "9000": 0.029044, "10000": 0.042676, "20000": 0.072157, "30000": 0.112447, "40000": 0.155155,
    "50000": 0.222948, "60000": 0.288275, "70000": 0.283510, "80000": 0.374177, "90000": 0.374333,
    "100000": 0.439167
}

data_cpp = {
    "100": 0.0, "500": 0.000939, "1000": 0.000998, "2000": 0.000984, "3000": 0.000912, 
    "4000": 0.001929, "5000": 0.003064, "6000": 0.001935, "7000": 0.003991, "8000": 0.001994,
    "9000": 0.004986, "10000": 0.005888, "20000": 0.007190, "30000": 0.018949, "40000": 0.028922,
    "50000": 0.020944, "60000": 0.030883, "70000": 0.042884, "80000": 0.053876, "90000": 0.053924,
    "100000": 0.046874
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
plt.title('Comparación de tiempos de Heap Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

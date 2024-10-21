import matplotlib.pyplot as plt

# Datos de ejecución de Selection Sort para Java, Python y C++
data_java = {
    "100": 9.19E-5, "500": 7.11E-5, "1000": 0.0052906, "2000": 0.0016678, "3000": 0.0021425,
    "4000": 0.0035352, "5000": 0.0052984, "6000": 0.0078362, "7000": 0.0114615, "8000": 0.0158484,
    "9000": 0.0172622, "10000": 0.0455515, "20000": 0.094361, "30000": 0.1951083, "40000": 0.3333957,
    "50000": 0.5415501, "60000": 0.8868314, "70000": 1.1241807, "80000": 1.4630144, "90000": 1.9712653,
    "100000": 2.2083265
}

data_python = {
    "100": 0.000707, "500": 0.005046, "1000": 0.070138, "2000": 0.085767, "3000": 0.189986,
    "4000": 0.338601, "5000": 0.530472, "6000": 0.756726, "7000": 1.322200, "8000": 1.351493,
    "9000": 4.111435, "10000": 2.464471, "20000": 8.495437, "30000": 19.225581, "40000": 34.890320,
    "50000": 54.353050, "60000": 83.474571, "70000": 106.987668, "80000": 182.192795, "90000": 412.970137,
    "100000": 247.817018
}

data_cpp = {
    "100": 0.0, "500": 0.001021, "1000": 0.003161, "2000": 0.011522, "3000": 0.023526,
    "4000": 0.043125, "5000": 0.068365, "6000": 0.092308, "7000": 0.128191, "8000": 0.163775,
    "9000": 0.212895, "10000": 0.275559, "20000": 1.028255, "30000": 2.317188, "40000": 4.163092,
    "50000": 6.512892, "60000": 9.387447, "70000": 12.720471, "80000": 16.630792, "90000": 21.333072,
    "100000": 26.014812
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
plt.title('Comparación de tiempos de Selection Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

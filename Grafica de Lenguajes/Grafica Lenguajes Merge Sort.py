import matplotlib.pyplot as plt

# Datos de ejecución de Merge Sort para Java, Python y C++
data_java = {
    "100": 1.996E-4, "500": 6.43E-5, "1000": 0.0020905, "2000": 2.579E-4, "3000": 3.275E-4,
    "4000": 4.844E-4, "5000": 6.577E-4, "6000": 0.0012037, "7000": 8.542E-4, "8000": 0.0011545,
    "9000": 0.0010955, "10000": 0.0061822, "20000": 0.0024322, "30000": 0.0038347, "40000": 0.0081346,
    "50000": 0.0074411, "60000": 0.0079821, "70000": 0.0123713, "80000": 0.0146152, "90000": 0.0119168,
    "100000": 0.0180706
}

data_python = {
    "100": 0.000641, "500": 0.000830, "1000": 0.007854, "2000": 0.015199, "3000": 0.006562,
    "4000": 0.009002, "5000": 0.011650, "6000": 0.014358, "7000": 0.017041, "8000": 0.019502,
    "9000": 0.022346, "10000": 0.044128, "20000": 0.059700, "30000": 0.085014, "40000": 0.118774,
    "50000": 0.149631, "60000": 0.181332, "70000": 0.317485, "80000": 0.250497, "90000": 0.286206,
    "100000": 0.514797
}

data_cpp = {
    "100": 0.0, "500": 0.0, "1000": 0.001007, "2000": 0.002045, "3000": 0.003987,
    "4000": 0.005984, "5000": 0.002733, "6000": 0.005648, "7000": 0.008974, "8000": 0.014226,
    "9000": 0.009972, "10000": 0.011897, "20000": 0.027977, "30000": 0.041887, "40000": 0.026929,
    "50000": 0.035881, "60000": 0.078631, "70000": 0.096714, "80000": 0.109702, "90000": 0.125432,
    "100000": 0.148202
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
plt.title('Comparación de tiempos de Merge Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

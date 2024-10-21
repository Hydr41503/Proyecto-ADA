import matplotlib.pyplot as plt

# Datos de ejecución de Insertion Sort para Java, Python y C++
data_java = {
    "100": 9.87E-5, "500": 5.99E-5, "1000": 0.0076161, "2000": 7.336E-4, "3000": 0.0028415, 
    "4000": 0.0047997, "5000": 0.0046978, "6000": 0.0098529, "7000": 0.0089465, "8000": 0.0116621,
    "9000": 0.0071939, "10000": 0.0472174, "20000": 0.0931124, "30000": 0.2191978, "40000": 0.3302256,
    "50000": 0.5004716, "60000": 0.7935152, "70000": 0.971466, "80000": 0.7463013, "90000": 0.8264293,
    "100000": 3.9261456
}

data_python = {
    "100": 0.000155, "500": 0.004855, "1000": 0.019797, "2000": 0.070980, "3000": 0.165630, 
    "4000": 0.289865, "5000": 0.538972, "6000": 0.674721, "7000": 0.933207, "8000": 1.203463,
    "9000": 1.659778, "10000": 1.912355, "20000": 7.394345, "30000": 17.271560, "40000": 30.420827,
    "50000": 47.351971, "60000": 68.877781, "70000": 93.626544, "80000": 122.392347, "90000": 154.767526,
    "100000": 189.433495
}

data_cpp = {
    "100": 0.0, "500": 0.0, "1000": 0.003298, "2000": 0.006018, "3000": 0.014585, 
    "4000": 0.032215, "5000": 0.090278, "6000": 0.097079, "7000": 0.079738, "8000": 0.161734,
    "9000": 0.185981, "10000": 0.301204, "20000": 0.653694, "30000": 1.536988, "40000": 3.127537,
    "50000": 4.666240, "60000": 6.809441, "70000": 9.035628, "80000": 11.192223, "90000": 15.127766,
    "100000": 18.054608
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
plt.title('Comparación de tiempos de Insertion Sort entre Java, Python y C++')

# Mostrar leyenda y rejilla
plt.legend()
plt.grid(True)
plt.xticks(file_sizes, rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()

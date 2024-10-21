import matplotlib.pyplot as plt

# Datos
números_de_datos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 
                    10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 
                    100000]
tiempos_bubble_sort = [0.000332, 0.009760, 0.040197, 0.153196, 0.369810, 0.635313, 
                       1.020118, 1.501205, 2.187337, 2.647402, 3.323562, 4.187162, 
                       17.122473, 38.178192, 67.018961, 106.643915, 152.308326, 
                       206.943345, 275.157913, 343.000718, 423.834101]
tiempos_counting_sort = [0.000028, 0.000124, 0.000208, 0.000434, 0.000587, 0.000788, 
                         0.001108, 0.001262, 0.001481, 0.001621, 0.002047, 0.002084, 
                         0.003960, 0.006189, 0.008536, 0.010481, 0.012808, 
                         0.016620, 0.018709, 0.018550, 0.021034]
tiempos_heap_sort = [0.000133, 0.000947, 0.001944, 0.004128, 0.006803, 0.009161, 
                     0.013284, 0.015032, 0.017829, 0.020530, 0.025842, 0.026200, 
                     0.056420, 0.090984, 0.125498, 0.155359, 0.192220, 
                     0.255225, 0.272592, 0.307142, 0.332279]
tiempos_insertion_sort = [0.000155, 0.004855, 0.019797, 0.070980, 0.165630, 0.289865, 
                          0.538972, 0.674721, 0.933207, 1.203463, 1.659778, 1.912355, 
                          7.394345, 17.271560, 30.420827, 47.351971, 68.877781, 
                          93.626544, 122.392347, 154.767526, 189.433495]
tiempos_merge_sort = [0.000123, 0.000797, 0.001698, 0.004461, 0.005204, 0.007221, 
                      0.010506, 0.011280, 0.013653, 0.015486, 0.020731, 0.020162, 
                      0.049193, 0.068255, 0.100241, 0.120066, 0.150958, 
                      0.174018, 0.202466, 0.231513, 0.258859]
tiempos_quick_sort = [0.000092, 0.000421, 0.000713, 0.001197, 0.001582, 0.002160, 
                      0.003083, 0.003244, 0.003963, 0.004634, 0.005510, 0.005552, 
                      0.011701, 0.016247, 0.024488, 0.028152, 0.035284, 
                      0.040972, 0.045463, 0.043480, 0.052510]
tiempos_selection_sort = [0.000160, 0.004930, 0.018937, 0.071732, 0.160348, 0.284719, 
                          0.514806, 0.648023, 0.905227, 1.163229, 1.532472, 1.787018, 
                          7.536679, 16.678778, 29.349717, 45.599709, 67.347815, 
                          92.703414, 119.161479, 147.153680, 191.889751]

# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(números_de_datos, tiempos_bubble_sort, label='Bubble Sort', marker='o')
plt.plot(números_de_datos, tiempos_counting_sort, label='Counting Sort', marker='o')
plt.plot(números_de_datos, tiempos_heap_sort, label='Heap Sort', marker='o')
plt.plot(números_de_datos, tiempos_insertion_sort, label='Insertion Sort', marker='o')
plt.plot(números_de_datos, tiempos_merge_sort, label='Merge Sort', marker='o')
plt.plot(números_de_datos, tiempos_quick_sort, label='Quick Sort', marker='o')
plt.plot(números_de_datos, tiempos_selection_sort, label='Selection Sort', marker='o')

# Configuración de la gráfica
plt.title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento')
plt.xlabel('Cantidad de Datos')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xscale('log')  # Escala logarítmica para el eje x
plt.yscale('log')  # Escala logarítmica para el eje y
plt.legend()
plt.grid()
plt.tight_layout()

# Mostrar la gráfica
plt.show()

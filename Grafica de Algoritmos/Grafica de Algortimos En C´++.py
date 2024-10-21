import matplotlib.pyplot as plt

# Tamaños de los datos
números_de_datos = [
    100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
    10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000
]

# Tiempos de ejecución para cada algoritmo (en segundos)
tiempos_bubble_sort = [
    0, 0.0129420000, 0.0265674000, 0.0645619000, 0.1169098000,
    0.1867559000, 0.2688737000, 0.3651452000, 0.4748697000, 0.6410620000,
    0.7750378000, 2.9760564000, 6.7463531000, 11.9301421000, 18.7778840000,
    26.8907014000, 36.6939473000, 47.8921003000, 60.4531757000, 74.6791282000
]

tiempos_counting_sort = [
    0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0.0207018000,
    0.0080331000, 0.0081024000, 0.0080387000, 0, 0.0090767000
]

tiempos_heap_sort = [
    0.0010461000, 0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0.0081557000, 0.0080817000, 0.0161252000, 0.0207018000,
    0.0242260000, 0.0323057000, 0.0333178000, 0.0406857000, 0.0486135000, 0
]

tiempos_insertion_sort = [
    0.0000000000, 0.0083417000, 0.0083337000, 0.0171621000, 0.0252776000,
    0.0403962000, 0.0571205000, 0.0817965000, 0.1019079000, 0.1284523000,
    0.1607923000, 0.6362389000, 1.4378827000, 2.6022907000, 4.0062114000,
    5.7798785000, 7.8533966000, 10.3205407000, 13.0424851000, 16.0146968000
]

tiempos_merge_sort = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0.0081448000, 0.0081542000,
    0.0081375000, 0.0161616000, 0.0241709000, 0.0252403000, 0.0325517000,
    0.0327089000, 0.0404077000, 0.0643924000, 0.0568951000, 0.0541379000
]

tiempos_quick_sort = [
    0, 0, 0, 0, 0,
    0, 0.0080804000, 0., 0, 0,
    0, 0, 0.0098206000, 0.0306946000, 0.0355272000,
    0.0565027000, 0.0646490000, 0.0884103000, 0.1141114000, 0.1376824000
]

tiempos_selection_sort = [
    0.0000000000, 0.0077542000, 0.0091610000, 0.0243225000, 0.0484225000,
    0.0755672000, 0.1075520000, 0.1564426000, 0.2008397000, 0.2485744000,
    0.3048023000, 1.2216300000, 2.7624919000, 4.9176807000, 7.6767572000,
    11.1204446000, 15.2559841000, 19.6809925000, 24.9113682000, 30.8466392000
]

# Graficar
plt.figure(figsize=(14, 8))

# Graficar cada algoritmo
plt.plot(números_de_datos, tiempos_bubble_sort, label='Bubble Sort', marker='o')
plt.plot(números_de_datos, tiempos_counting_sort, label='Counting Sort', marker='o')
plt.plot(números_de_datos, tiempos_heap_sort, label='Heap Sort', marker='o')
plt.plot(números_de_datos, tiempos_insertion_sort, label='Insertion Sort', marker='o')
plt.plot(números_de_datos, tiempos_merge_sort, label='Merge Sort', marker='o')
plt.plot(números_de_datos, tiempos_quick_sort, label='Quick Sort', marker='o')
plt.plot(números_de_datos, tiempos_selection_sort, label='Selection Sort', marker='o')

# Configuraciones de la gráfica
plt.title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento')
plt.xlabel('Tamaño de Datos (número de elementos)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xscale('log')  # Escala logarítmica para el eje x
plt.yscale('log')  # Escala logarítmica para el eje y
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.xticks(números_de_datos, rotation=45)

# Mostrar gráfica
plt.tight_layout()
plt.show()

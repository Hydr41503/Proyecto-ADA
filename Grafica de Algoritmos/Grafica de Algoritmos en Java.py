import matplotlib.pyplot as plt
import numpy as np

# Datos de tiempo de ejecución de los algoritmos en Java
data_java = {
    "100": {"Bubble Sort": 3.177E-4, "Merge Sort": 9.56E-5, "Counting Sort": 0.0020956, "Insertion Sort": 8.21E-5, "Heap Sort": 1.159E-4, "Quick Sort": 4.69E-5, "Selection Sort": 1.403E-4},
    "1000": {"Bubble Sort": 0.0144958, "Merge Sort": 0.0014684, "Counting Sort": 4.407E-4, "Insertion Sort": 0.002955, "Heap Sort": 3.545E-4, "Quick Sort": 5.671E-4, "Selection Sort": 0.0044799},
    "2000": {"Bubble Sort": 0.0036135, "Merge Sort": 2.152E-4, "Counting Sort": 7.4E-5, "Insertion Sort": 3.335E-4, "Heap Sort": 1.896E-4, "Quick Sort": 9.17E-5, "Selection Sort": 0.0010887},
    "3000": {"Bubble Sort": 0.008136, "Merge Sort": 3.372E-4, "Counting Sort": 2.0E-4, "Insertion Sort": 7.24E-4, "Heap Sort": 2.72E-4, "Quick Sort": 1.424E-4, "Selection Sort": 0.0023794},
    "4000": {"Bubble Sort": 0.0155336, "Merge Sort": 4.412E-4, "Counting Sort": 4.23E-4, "Insertion Sort": 0.0012491, "Heap Sort": 3.673E-4, "Quick Sort": 1.978E-4, "Selection Sort": 0.004188},
    "5000": {"Bubble Sort": 0.025886, "Merge Sort": 0.0024853, "Counting Sort": 1.592E-4, "Insertion Sort": 0.0021707, "Heap Sort": 5.118E-4, "Quick Sort": 2.962E-4, "Selection Sort": 0.0077092},
    "6000": {"Bubble Sort": 0.038676, "Merge Sort": 6.747E-4, "Counting Sort": 1.769E-4, "Insertion Sort": 0.0028257, "Heap Sort": 5.981E-4, "Quick Sort": 3.34E-4, "Selection Sort": 0.0092191},
    "7000": {"Bubble Sort": 0.0545457, "Merge Sort": 7.779E-4, "Counting Sort": 5.44E-5, "Insertion Sort": 0.003872, "Heap Sort": 6.161E-4, "Quick Sort": 3.999E-4, "Selection Sort": 0.0125044},
    "8000": {"Bubble Sort": 0.0733084, "Merge Sort": 0.0010948, "Counting Sort": 6.91E-5, "Insertion Sort": 0.004998, "Heap Sort": 7.113E-4, "Quick Sort": 4.877E-4, "Selection Sort": 0.0162631},
    "9000": {"Bubble Sort": 0.0970313, "Merge Sort": 0.0010678, "Counting Sort": 6.55E-5, "Insertion Sort": 0.0063278, "Heap Sort": 8.028E-4, "Quick Sort": 5.768E-4, "Selection Sort": 0.0205438},
    "10000": {"Bubble Sort": 0.1533931, "Merge Sort": 0.002107, "Counting Sort": 0.0014599, "Insertion Sort": 0.0358552, "Heap Sort": 0.0015057, "Quick Sort": 0.0026283, "Selection Sort": 0.0465123},
    "20000": {"Bubble Sort": 0.5589329, "Merge Sort": 0.0022801, "Counting Sort": 3.92E-4, "Insertion Sort": 0.033017, "Heap Sort": 0.0019784, "Quick Sort": 0.0018486, "Selection Sort": 0.1004943},
    "30000": {"Bubble Sort": 1.4354683, "Merge Sort": 0.0035627, "Counting Sort": 4.348E-4, "Insertion Sort": 0.0760713, "Heap Sort": 0.0030338, "Quick Sort": 0.003552, "Selection Sort": 0.2254925},
    "40000": {"Bubble Sort": 2.3559242, "Merge Sort": 0.0048533, "Counting Sort": 3.553E-4, "Insertion Sort": 0.1353628, "Heap Sort": 0.0039118, "Quick Sort": 0.0057522, "Selection Sort": 0.4381406},
    "50000": {"Bubble Sort": 3.8721075, "Merge Sort": 0.0059041, "Counting Sort": 4.993E-4, "Insertion Sort": 0.2131302, "Heap Sort": 0.0049139, "Quick Sort": 0.0084414, "Selection Sort": 0.6240037},
    "60000": {"Bubble Sort": 5.338902, "Merge Sort": 0.0074286, "Counting Sort": 5.271E-4, "Insertion Sort": 0.3092488, "Heap Sort": 0.0058198, "Quick Sort": 0.0116135, "Selection Sort": 0.9436481},
    "70000": {"Bubble Sort": 7.2692359, "Merge Sort": 0.0101764, "Counting Sort": 4.22E-4, "Insertion Sort": 0.4207243, "Heap Sort": 0.0068112, "Quick Sort": 0.0151609, "Selection Sort": 1.2254249},
    "80000": {"Bubble Sort": 9.7359474, "Merge Sort": 0.0131351, "Counting Sort": 4.6E-4, "Insertion Sort": 0.6455874, "Heap Sort": 0.0078658, "Quick Sort": 0.0193062, "Selection Sort": 1.6372561},
    "90000": {"Bubble Sort": 12.197449, "Merge Sort": 0.0105819, "Counting Sort": 3.95E-4, "Insertion Sort": 0.7013472, "Heap Sort": 0.0088466, "Quick Sort": 0.0239752, "Selection Sort": 2.0229322},
    "100000": {"Bubble Sort": 15.0807548, "Merge Sort": 0.0166073, "Counting Sort": 0.0062809, "Insertion Sort": 2.8257093, "Heap Sort": 0.0116072, "Quick Sort": 0.0304892, "Selection Sort": 2.5517767},
}

# Extraer los nombres de archivos y los tiempos de ejecución
files = sorted(data_java.keys(), key=lambda x: int(x.replace('-', '').replace('.', '')))
bubble_sort = [data_java[file]["Bubble Sort"] for file in files]
merge_sort = [data_java[file]["Merge Sort"] for file in files]
counting_sort = [data_java[file]["Counting Sort"] for file in files]
insertion_sort = [data_java[file]["Insertion Sort"] for file in files]
heap_sort = [data_java[file]["Heap Sort"] for file in files]
quick_sort = [data_java[file]["Quick Sort"] for file in files]
selection_sort = [data_java[file]["Selection Sort"] for file in files]

# Crear la figura y los ejes
plt.figure(figsize=(12, 6))

# Graficar los datos
plt.plot(files, bubble_sort, marker='o', label='Bubble Sort')
plt.plot(files, merge_sort, marker='o', label='Merge Sort')
plt.plot(files, counting_sort, marker='o', label='Counting Sort')
plt.plot(files, insertion_sort, marker='o', label='Insertion Sort')
plt.plot(files, heap_sort, marker='o', label='Heap Sort')
plt.plot(files, quick_sort, marker='o', label='Quick Sort')
plt.plot(files, selection_sort, marker='o', label='Selection Sort')

# Configurar los ejes
plt.xlabel('Tamaño de Datos (archivos)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Algoritmos de Ordenamiento en Java')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()

# Mostrar el gráfico
plt.show()

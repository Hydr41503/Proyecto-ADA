import time
import os
import csv

# Algoritmos de ordenamiento

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Leer los números de un archivo
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        cleaned_content = ''.join(c for c in content if c.isdigit() or c.isspace() or c == '-')
        numbers = list(map(int, cleaned_content.split()))
    return numbers

# Medir el tiempo de ejecución de un algoritmo
def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Copia del arreglo para no modificar el original
    end_time = time.time()
    return end_time - start_time

# Guardar resultados en un archivo CSV
def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Archivo', 'Heap Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timing in results.items():
            writer.writerow({'Archivo': file, 'Heap Sort': timing})

# Función principal
def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'  # Cambiar a la ruta adecuada
    results = {}

    # Iterar sobre los archivos de la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)

            # Medir el tiempo de ejecución del Heap Sort
            duration = measure_sort_time(heap_sort, numbers)
            results[filename] = duration

    # Guardar los resultados en un archivo CSV
    save_results_to_csv(results, 'resultados_heap_sort.csv')

    # Mostrar los resultados por pantalla
    for file, time_taken in results.items():
        print(f"Resultados para {file}:")
        print(f"Heap Sort: {time_taken:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

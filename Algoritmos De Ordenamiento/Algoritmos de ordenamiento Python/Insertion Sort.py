import time
import os
import csv

# Algoritmo de ordenamiento Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Leer números de un archivo
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        cleaned_content = ''.join(c for c in content if c.isdigit() or c.isspace() or c == '-')
        numbers = list(map(int, cleaned_content.split()))
    return numbers

# Medir el tiempo de ejecución de un algoritmo
def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy()) 
    end_time = time.time()
    return end_time - start_time

# Guardar resultados en un archivo CSV
def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Archivo', 'Insertion Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timings in results.items():
            row = {'Archivo': file, 'Insertion Sort': timings['Insertion Sort']}
            writer.writerow(row)

# Función principal
def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'  # Ruta de la carpeta que contiene los archivos de datos
    
    results = {}

    # Iterar sobre los archivos
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            file_results = {}

            # Medir el tiempo solo de Insertion Sort
            duration = measure_sort_time(insertion_sort, numbers)
            file_results['Insertion Sort'] = duration
            results[filename] = file_results
    
    # Guardar los resultados en un archivo CSV
    save_results_to_csv(results, 'resultados_insertion_sort.csv')

    # Imprimir los resultados
    for file, timings in results.items():
        print(f"Resultados para {file}:")
        print(f"Insertion Sort: {timings['Insertion Sort']:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

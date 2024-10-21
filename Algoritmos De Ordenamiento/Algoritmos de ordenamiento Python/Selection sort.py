import time
import os
import csv

# Algoritmo de ordenamiento: Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        cleaned_content = ''.join(c for c in content if c.isdigit() or c.isspace() or c == '-')
        numbers = list(map(int, cleaned_content.split()))
    return numbers

def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Archivo', 'Selection Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timings in results.items():
            row = {'Archivo': file, 'Selection Sort': timings['Selection Sort']}
            writer.writerow(row)

def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'
    
    results = {}

    # Iterar sobre los archivos
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            duration = measure_sort_time(selection_sort, numbers)
            results[filename] = {'Selection Sort': duration}

    save_results_to_csv(results, 'resultados_python.csv')

    for file, timings in results.items():
        print(f"Resultados para {file}:")
        print(f"Selection Sort: {timings['Selection Sort']:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

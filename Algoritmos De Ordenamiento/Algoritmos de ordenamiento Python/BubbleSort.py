import time
import os
import csv

# Algoritmo de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
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
        fieldnames = ['Archivo', 'Bubble Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timings in results.items():
            row = {'Archivo': file, 'Bubble Sort': timings['Bubble Sort']}
            writer.writerow(row)

def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'  
    results = {}

    # Iterar sobre los archivos
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            duration = measure_sort_time(bubble_sort, numbers)
            results[filename] = {'Bubble Sort': duration}

    save_results_to_csv(results, 'resultados_python.csv')

    for file, timings in results.items():
        print(f"Resultados para {file}:")
        print(f"Bubble Sort: {timings['Bubble Sort']:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

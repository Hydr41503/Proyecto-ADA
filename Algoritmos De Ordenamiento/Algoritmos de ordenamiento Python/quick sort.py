import time
import os
import csv

# Algoritmo de Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

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
        fieldnames = ['Archivo', 'Quick Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timings in results.items():
            row = {'Archivo': file, 'Quick Sort': timings['Quick Sort']}
            writer.writerow(row)

def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'  
    results = {}

    # Iterar sobre los archivos
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            duration = measure_sort_time(quick_sort, numbers)
            results[filename] = {'Quick Sort': duration}

    save_results_to_csv(results, 'resultados_quick_sort.csv')

    for file, timings in results.items():
        print(f"Resultados para {file}:")
        print(f"Quick Sort: {timings['Quick Sort']:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

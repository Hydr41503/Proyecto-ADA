import time
import os
import csv

# Algoritmos de ordenamiento

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

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
        fieldnames = ['Archivo', 'Counting Sort']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file, timing in results.items():
            writer.writerow({'Archivo': file, 'Counting Sort': timing})

def main():
    folder_path = r'C:\Users\saulj\Downloads\ADA_DATOS-main'  
    results = {}

    # Iterar sobre los archivos
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            numbers = read_numbers_from_file(file_path)
            duration = measure_sort_time(counting_sort, numbers)
            results[filename] = duration
    
    save_results_to_csv(results, 'resultados_counting_sort.csv')

    for file, time_taken in results.items():
        print(f"Resultados para {file}:")
        print(f"Counting Sort: {time_taken:.6f} segundos")
        print()

if __name__ == "__main__":
    main()

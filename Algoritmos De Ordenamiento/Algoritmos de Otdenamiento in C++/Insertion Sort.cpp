#include <string>
#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iomanip> // Para std::setprecision
#include <dirent.h> // Para manejar directorios

// Algoritmos de ordenamiento

// Bubble Sort
void bubbleSort(std::vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; i++) {
        for (size_t j = 0; j < arr.size() - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Counting Sort
void countingSort(std::vector<int>& arr) {
    int max_val = *max_element(arr.begin(), arr.end());
    int min_val = *min_element(arr.begin(), arr.end());
    int range = max_val - min_val + 1;

    std::vector<int> count(range), output(arr.size());

    for (int num : arr)
        count[num - min_val]++;

    for (size_t i = 1; i < count.size(); i++)
        count[i] += count[i - 1];

    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i] - min_val] - 1] = arr[i];
        count[arr[i] - min_val]--;
    }

    arr = output;
}

// Heap Sort
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int>& arr) {
    int n = arr.size();

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

// Insertion Sort
void insertionSort(std::vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Merge Sort
void merge(std::vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

// Quick Sort
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSortHelper(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortHelper(arr, low, pi - 1);
        quickSortHelper(arr, pi + 1, high);
    }
}

void quickSort(std::vector<int>& arr) {
    quickSortHelper(arr, 0, arr.size() - 1);
}

// Selection Sort
void selectionSort(std::vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; i++) {
        size_t min_idx = i;
        for (size_t j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[min_idx], arr[i]);
    }
}

// Leer números de archivo
std::vector<int> readNumbersFromFile(const std::string& file_path) {
    std::ifstream file(file_path);
    std::vector<int> numbers;
    std::string line;

    if (!file) {
        std::cerr << "Error al abrir el archivo: " << file_path << std::endl;
        return numbers; // Retorna un vector vacío si no se puede abrir el archivo
    }

    while (std::getline(file, line)) {
        // Remover corchetes y espacios
        line.erase(std::remove(line.begin(), line.end(), '['), line.end());
        line.erase(std::remove(line.begin(), line.end(), ']'), line.end());
        line.erase(std::remove(line.begin(), line.end(), ' '), line.end());

        std::stringstream ss(line);
        int num;
        char comma; // Variable para leer las comas

        // Leer números separados por comas
        while (ss >> num) {
            numbers.push_back(num);
            ss >> comma; // Ignorar la coma
        }
    }

    std::cout << "Número de elementos en el archivo " << file_path << ": " << numbers.size() << std::endl;

    return numbers;
}

// Medir el tiempo de ejecución del algoritmo de ordenamiento
double measureSortTime(const std::function<void(std::vector<int>&)>& sort_func, std::vector<int> numbers) {
    auto start = std::chrono::high_resolution_clock::now();
    sort_func(numbers);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    return duration.count();
}

// Función principal
int main() {
    std::string folder_path = "C:/Users/saulj/Downloads/ADA_DATOS-main";  // Ruta de la carpeta con los archivos txt

    std::map<std::string, std::function<void(std::vector<int>&)>> algorithms = {
        {"Insertion Sort", insertionSort}, // Solo se mantiene Insertion Sort
    };

    std::map<std::string, std::map<std::string, double>> results;

    // Obtener archivos .txt en el directorio
    DIR* dir;
    struct dirent* ent;
    std::vector<std::string> txt_files;

    if ((dir = opendir(folder_path.c_str())) != nullptr) {
        while ((ent = readdir(dir)) != nullptr) {
            std::string file_name = ent->d_name;
            if (file_name.find(".txt") != std::string::npos) {
                txt_files.push_back(folder_path + "\\" + file_name); // Agregar la ruta completa
            }
        }
        closedir(dir);
    } else {
        std::cerr << "No se pudo abrir el directorio\n";
    }

    for (const auto& file_path : txt_files) {
        std::vector<int> numbers = readNumbersFromFile(file_path);

        std::map<std::string, double> timings;

        for (const auto& algorithm : algorithms) {
            double time_taken = measureSortTime(algorithm.second, numbers);
            timings[algorithm.first] = time_taken;
        }

        std::string file_name = file_path.substr(file_path.find_last_of("\\") + 1); // Obtener el nombre del archivo
        results[file_name] = timings;
    }

    // Imprimir resultados solo para Insertion Sort
    std::cout << "Resultados de Insertion Sort:\n";
    for (const auto& result : results) {
        std::cout << result.first << " : " << std::fixed << std::setprecision(6) << result.second.at("Insertion Sort") << " segundos\n";
    }

    return 0;
}



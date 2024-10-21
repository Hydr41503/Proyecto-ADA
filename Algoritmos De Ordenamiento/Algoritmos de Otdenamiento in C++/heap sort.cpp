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
        line.erase(remove(line.begin(), line.end(), '['), line.end());
        line.erase(remove(line.begin(), line.end(), ']'), line.end());
        line.erase(remove(line.begin(), line.end(), ' '), line.end());

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

// Guardar resultados en CSV
void saveResultsToCSV(const std::map<std::string, std::map<std::string, double>>& results, const std::string& output_file) {
    std::ofstream csvFile(output_file);
    csvFile << "Archivo,Heap Sort\n";

    for (const auto &result : results) {
        csvFile << result.first;
        for (const auto& timing : result.second) {
            csvFile << "," << timing.second;
        }
        csvFile << "\n";
    }

    csvFile.close();
}

// Función para obtener archivos .txt de un directorio
std::vector<std::string> getFilesInDirectory(const std::string& folder_path) {
    std::vector<std::string> txt_files;
    DIR* dir;
    struct dirent* ent;

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

    return txt_files;
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
        {"Heap Sort", heapSort}
    };

    std::map<std::string, std::map<std::string, double>> results;

    // Obtén archivos .txt en el directorio
    std::vector<std::string> txt_files = getFilesInDirectory(folder_path);

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

    // Guardar resultados en CSV
    saveResultsToCSV(results, "resultados_heap_sort.csv");

    std::cout << "Resultados guardados en resultados_heap_sort.csv" << std::endl;

    // Imprimir resultados en formato array
    for (const auto& result : results) {
        std::cout << result.first << " : { ";
        for (const auto& timing : result.second) {
            std::cout << "\"" << timing.first << "\": " << std::fixed << std::setprecision(6) << timing.second << ", ";
        }
        std::cout << "}\n";
    }

    return 0;
}


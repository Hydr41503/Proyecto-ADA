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

// Algoritmo de ordenamiento: Selection Sort
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

// Medir el tiempo de ejecución del algoritmo de ordenamiento
double measureSortTime(const std::function<void(std::vector<int>&)>& sort_func, std::vector<int> numbers) {
    auto start = std::chrono::high_resolution_clock::now();
    sort_func(numbers);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    return duration.count();
}

// Guardar resultados en CSV
void saveResultsToCSV(const std::map<std::string, double>& results, const std::string& output_file) {
    std::ofstream csvFile(output_file);
    csvFile << "Archivo,Selection Sort\n";

    for (const auto &result : results) {
        csvFile << result.first << "," << result.second << "\n";
    }

    csvFile.close();
}

// Función principal
int main() {
    std::string folder_path = "C:/Users/saulj/Downloads/ADA_DATOS-main";  // Ruta de la carpeta con los archivos txt

    std::map<std::string, double> results;

    // Obtener archivos .txt en el directorio
    DIR* dir;
    struct dirent* ent;
    if ((dir = opendir(folder_path.c_str())) != nullptr) {
        while ((ent = readdir(dir)) != nullptr) {
            std::string file_name = ent->d_name;
            if (file_name.find(".txt") != std::string::npos) {
                std::string file_path = folder_path + "\\" + file_name; // Agregar la ruta completa
                std::vector<int> numbers = readNumbersFromFile(file_path);

                double time_taken = measureSortTime(selectionSort, numbers);
                results[file_name] = time_taken;
            }
        }
        closedir(dir);
    } else {
        std::cerr << "No se pudo abrir el directorio\n";
    }

    // Guardar resultados en CSV
    saveResultsToCSV(results, "resultados_selection_sort.csv");

    std::cout << "Resultados guardados en resultados_selection_sort.csv" << std::endl;

    // Imprimir resultados
    for (const auto& result : results) {
        std::cout << result.first << " : " << std::fixed << std::setprecision(6) << result.second << " segundos\n";
    }

    return 0;
}


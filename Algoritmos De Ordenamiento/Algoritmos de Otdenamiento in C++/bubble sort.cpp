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

// Algoritmo de ordenamiento Bubble Sort
void bubbleSort(std::vector<int>& arr) {
    for (size_t i = 0; i < arr.size() - 1; i++) {
        for (size_t j = 0; j < arr.size() - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
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
void saveResultsToCSV(const std::map<std::string, double>& results, const std::string& output_file) {
    std::ofstream csvFile(output_file);
    csvFile << "Archivo,Bubble Sort\n";

    for (const auto &result : results) {
        csvFile << result.first << "," << result.second << "\n";
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

// Medir el tiempo de ejecución del algoritmo de Bubble Sort
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

    std::map<std::string, double> results;

    // Obtén archivos .txt en el directorio
    std::vector<std::string> txt_files = getFilesInDirectory(folder_path);

    for (const auto& file_path : txt_files) {
        std::vector<int> numbers = readNumbersFromFile(file_path);

        // Medir tiempo de ejecución de Bubble Sort
        double time_taken = measureSortTime(bubbleSort, numbers);

        std::string file_name = file_path.substr(file_path.find_last_of("\\") + 1); // Obtener el nombre del archivo
        results[file_name] = time_taken;
    }

    // Guardar resultados en CSV
    saveResultsToCSV(results, "resultados_bubble_sort.csv");

    std::cout << "Resultados guardados en resultados_bubble_sort.csv" << std::endl;

    // Imprimir resultados en formato array
    for (const auto& result : results) {
        std::cout << result.first << " : { \"Bubble Sort\": " << std::fixed << std::setprecision(6) << result.second << " }\n";
    }

    return 0;
}


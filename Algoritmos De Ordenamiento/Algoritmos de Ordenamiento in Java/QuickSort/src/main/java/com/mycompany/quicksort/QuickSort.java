/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.quicksort;
import java.io.*;
import java.util.*;
import java.util.function.Consumer;
public class QuickSort {

   // Quick Sort
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return (i + 1);
    }

    // Swap helper function
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Leer números de un archivo
    public static int[] readNumbersFromFile(String filePath) {
        List<Integer> numbers = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.replaceAll("[\\[\\] ]", ""); // Eliminar corchetes y espacios
                String[] nums = line.split(",");
                for (String num : nums) {
                    numbers.add(Integer.parseInt(num));
                }
            }
        } catch (IOException e) {
            System.err.println("Error al abrir el archivo: " + filePath);
            e.printStackTrace();
        }
        return numbers.stream().mapToInt(i -> i).toArray();
    }

    // Medir el tiempo de ejecución
    public static double measureSortTime(Consumer<int[]> sortFunction, int[] arr) {
        long startTime = System.nanoTime();
        sortFunction.accept(arr);
        long endTime = System.nanoTime();
        return (endTime - startTime) / 1e9; // Convertir a segundos
    }

    public static void main(String[] args) {
        String folderPath = "C:\\Users\\saulj\\Downloads\\ADA_DATOS-main"; // Ruta de la carpeta

        Map<String, Consumer<int[]>> algorithms = new HashMap<>();
        algorithms.put("Quick Sort", arr -> quickSort(arr, 0, arr.length - 1));

        Map<String, Map<String, Double>> results = new HashMap<>();

        // Obtener archivos .txt en el directorio
        File folder = new File(folderPath);
        File[] txtFiles = folder.listFiles((dir, name) -> name.toLowerCase().endsWith(".txt"));

        if (txtFiles != null) {
            for (File file : txtFiles) {
                int[] numbers = readNumbersFromFile(file.getAbsolutePath());

                // Si el archivo tiene demasiados números, saltar
                if (numbers.length > 100000) {
                    System.err.println("Advertencia: El archivo " + file.getName() + " tiene demasiados números.");
                    continue;
                }

                Map<String, Double> fileResults = new HashMap<>();
                double duration = measureSortTime(algorithms.get("Quick Sort"), Arrays.copyOf(numbers, numbers.length));
                fileResults.put("Quick Sort", duration);

                results.put(file.getName(), fileResults);
            }
        }

        // Imprimir los resultados en formato de arreglo
        System.out.println("{");
        for (Map.Entry<String, Map<String, Double>> entry : results.entrySet()) {
            System.out.print("  \"" + entry.getKey() + "\": {");
            for (Map.Entry<String, Double> algorithm : entry.getValue().entrySet()) {
                System.out.print("\"" + algorithm.getKey() + "\": " + algorithm.getValue() + ", ");
            }
            System.out.println("},");
        }
        System.out.println("}");
    }
}

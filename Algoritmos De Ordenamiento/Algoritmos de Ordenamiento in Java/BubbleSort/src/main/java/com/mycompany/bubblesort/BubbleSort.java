
package com.mycompany.bubblesort;

import java.io.*;
import java.util.*;
import java.util.function.Consumer;

public class BubbleSort {
 
    // Bubble Sort
    public static void bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }
        }
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

        // Solo se necesita Bubble Sort
        Map<String, Consumer<int[]>> algorithms = new HashMap<>();
        algorithms.put("Bubble Sort", BubbleSort::bubbleSort);

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
                for (Map.Entry<String, Consumer<int[]>> entry : algorithms.entrySet()) {
                    double duration = measureSortTime(entry.getValue(), Arrays.copyOf(numbers, numbers.length));
                    fileResults.put(entry.getKey(), duration);
                }

                results.put(file.getName(), fileResults);
            }
        }

        // Imprimir los resultados en formato de arreglo
        printResultsAsArray(results);
    }

    // Imprimir resultados en formato de arreglo
    public static void printResultsAsArray(Map<String, Map<String, Double>> results) {
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

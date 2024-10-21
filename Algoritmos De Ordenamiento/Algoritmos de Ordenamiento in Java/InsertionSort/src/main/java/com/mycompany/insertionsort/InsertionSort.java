package com.mycompany.insertionsort;

import java.io.*;
import java.util.*;
import java.util.function.Consumer;
public class InsertionSort {

 public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
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

        Map<String, Consumer<int[]>> algorithms = new HashMap<>();
        algorithms.put("Insertion Sort", InsertionSort::insertionSort);

        Map<String, Double> results = new HashMap<>();

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

                double duration = measureSortTime(algorithms.get("Insertion Sort"), Arrays.copyOf(numbers, numbers.length));
                results.put(file.getName(), duration);
            }
        }

        // Imprimir los resultados en formato de arreglo
        System.out.println("{");
        for (Map.Entry<String, Double> entry : results.entrySet()) {
            System.out.println("  \"" + entry.getKey() + "\": " + entry.getValue() + ",");
        }
        System.out.println("}");
    }


}

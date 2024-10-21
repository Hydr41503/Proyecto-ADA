package com.mycompany.mergesort;

import java.io.*;
import java.util.*;
import java.util.function.Consumer;

public class MergeSort {

    // Merge Sort
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        System.arraycopy(arr, left, L, 0, n1);
        System.arraycopy(arr, mid + 1, R, 0, n2);

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while (i < n1) {
            arr[k++] = L[i++];
        }

        while (j < n2) {
            arr[k++] = R[j++];
        }
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

        // Obtener archivos .txt en el directorio
        File folder = new File(folderPath);
        File[] txtFiles = folder.listFiles((dir, name) -> name.toLowerCase().endsWith(".txt"));

        if (txtFiles != null) {
            for (File file : txtFiles) {
                int[] numbers = readNumbersFromFile(file.getAbsolutePath());

                // Medir el tiempo de ejecución del Merge Sort
                double duration = measureSortTime(arr -> mergeSort(arr, 0, arr.length - 1), Arrays.copyOf(numbers, numbers.length));

                // Imprimir el resultado
                System.out.println("Tiempo de ejecución de Merge Sort en " + file.getName() + ": " + duration + " segundos");
            }
        }
    }
}

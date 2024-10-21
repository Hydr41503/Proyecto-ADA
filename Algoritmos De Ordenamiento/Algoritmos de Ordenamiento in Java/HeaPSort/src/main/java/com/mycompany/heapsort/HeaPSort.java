
package com.mycompany.heapsort;

import java.io.*;
import java.util.*;
public class HeaPSort {

    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Construir el heap (reorganizar el arreglo)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extraer un elemento del heap uno por uno
        for (int i = n - 1; i > 0; i--) {
            swap(arr, 0, i);
            // Llamar heapify en el heap reducido
            heapify(arr, i, 0);
        }
    }

    // Función para heapificar un subárbol con la raíz en el índice i
    private static void heapify(int[] arr, int n, int i) {
        int largest = i;  // Inicializar el más grande como raíz
        int left = 2 * i + 1;  // hijo izquierdo
        int right = 2 * i + 2;  // hijo derecho

        // Si el hijo izquierdo es más grande que la raíz
        if (left < n && arr[left] > arr[largest])
            largest = left;

        // Si el hijo derecho es más grande que el mayor hasta ahora
        if (right < n && arr[right] > arr[largest])
            largest = right;

        // Si el más grande no es la raíz
        if (largest != i) {
            swap(arr, i, largest);

            // Recursivamente heapificar el subárbol afectado
            heapify(arr, n, largest);
        }
    }

    // Función para intercambiar dos elementos
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

    // Medir el tiempo de ejecución de Heap Sort
    public static double measureSortTime(int[] arr) {
        long startTime = System.nanoTime();
        heapSort(arr);
        long endTime = System.nanoTime();
        return (endTime - startTime) / 1e9; // Convertir a segundos
    }

    // Imprimir resultados
    public static void printResults(String fileName, double duration) {
        System.out.println("{\"" + fileName + "\": {\"Heap Sort\": " + duration + "}}");
    }

    public static void main(String[] args) {
        String folderPath = "C:\\Users\\saulj\\Downloads\\ADA_DATOS-main"; // Ruta de la carpeta

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

                // Medir el tiempo de Heap Sort
                double duration = measureSortTime(Arrays.copyOf(numbers, numbers.length));

                // Imprimir resultados
                printResults(file.getName(), duration);
            }
        } else {
            System.err.println("No se encontraron archivos en el directorio especificado.");
        }
    }
}

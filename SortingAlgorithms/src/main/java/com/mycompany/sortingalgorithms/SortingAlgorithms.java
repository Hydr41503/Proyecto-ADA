package com.mycompany.sortingalgorithms;

import java.io.*;
import java.util.*;
import java.util.function.Consumer;

public class SortingAlgorithms {

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

    // Counting Sort
    public static void countingSort(int[] arr) {
        int maxVal = Arrays.stream(arr).max().orElse(Integer.MAX_VALUE);
        int minVal = Arrays.stream(arr).min().orElse(Integer.MIN_VALUE);
        int range = maxVal - minVal + 1;

        int[] count = new int[range];
        int[] output = new int[arr.length];

        for (int num : arr) {
            count[num - minVal]++;
        }

        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[arr[i] - minVal] - 1] = arr[i];
            count[arr[i] - minVal]--;
        }

        System.arraycopy(output, 0, arr, 0, arr.length);
    }

    // Heap Sort
    public static void heapSort(int[] arr) {
        int n = arr.length;

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i > 0; i--) {
            swap(arr, 0, i);
            heapify(arr, i, 0);
        }
    }

    private static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest])
            largest = left;

        if (right < n && arr[right] > arr[largest])
            largest = right;

        if (largest != i) {
            swap(arr, i, largest);
            heapify(arr, n, largest);
        }
    }

    // Insertion Sort
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

    // Selection Sort
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            swap(arr, minIdx, i);
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
        algorithms.put("Bubble Sort", SortingAlgorithms::bubbleSort);
        algorithms.put("Counting Sort", SortingAlgorithms::countingSort);
        algorithms.put("Heap Sort", SortingAlgorithms::heapSort);
        algorithms.put("Insertion Sort", SortingAlgorithms::insertionSort);
        algorithms.put("Merge Sort", arr -> mergeSort(arr, 0, arr.length - 1));
        algorithms.put("Quick Sort", arr -> quickSort(arr, 0, arr.length - 1));
        algorithms.put("Selection Sort", SortingAlgorithms::selectionSort);

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
}
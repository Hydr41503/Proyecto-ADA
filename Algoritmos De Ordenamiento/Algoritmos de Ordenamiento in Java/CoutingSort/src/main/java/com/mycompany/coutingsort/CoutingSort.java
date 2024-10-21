package com.mycompany.coutingsort;

import java.io.*;
import java.util.*;

public class CoutingSort {

    // Implementación de Counting Sort
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
    public static double measureSortTime(int[] arr) {
        long startTime = System.nanoTime();
        countingSort(arr);
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

                // Si el archivo tiene demasiados números, saltar
                if (numbers.length > 100000) {
                    System.err.println("Advertencia: El archivo " + file.getName() + " tiene demasiados números.");
                    continue;
                }

                // Medir el tiempo de Counting Sort para cada archivo
                double duration = measureSortTime(Arrays.copyOf(numbers, numbers.length));
                System.out.println("Tiempo para " + file.getName() + ": " + duration + " segundos");
            }
        } else {
            System.err.println("No se encontraron archivos .txt en la carpeta.");
        }
    }
}

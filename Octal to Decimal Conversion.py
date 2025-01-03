import java.util.Scanner;

public class OctalToDecimal {
    public static void main(String[] args) {
        // Create a Scanner object to take input
        Scanner sc = new Scanner(System.in);

        // Input octal number as a string
        String octalString = sc.nextLine();

        // Convert the octal string to a decimal integer
        int decimalValue = Integer.parseInt(octalString, 8);

        // Output the result
        System.out.println(decimalValue);

        // Close the scanner
        sc.close();
    }
}
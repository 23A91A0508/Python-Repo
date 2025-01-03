import java.util.Scanner;

public class RomeoChocolates {
    public static void main(String[] args) {
        // Create a Scanner object to take input from user
        Scanner sc = new Scanner(System.in);

        // Input X, Y, Z
        int X = sc.nextInt();  // Number of 5 rupee coins
        int Y = sc.nextInt();  // Number of 10 rupee coins
        int Z = sc.nextInt();  // Cost of each chocolate
        
        // Calculate total money Romeo has
        int totalMoney = (X * 5) + (Y * 10);

        // Calculate the maximum number of chocolates Romeo can buy
        int maxChocolates = totalMoney / Z;
        
        // Output the result
        System.out.println(maxChocolates);
        
        // Close the scanner
        sc.close();
    }
}
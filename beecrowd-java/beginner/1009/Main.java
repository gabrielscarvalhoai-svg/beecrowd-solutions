/*
Beecrowd Problem 1009 - Salary with bonus
Category: Beginner
*/


import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main (String[] args) {

        Locale.setDefault(Locale.US);
        Scanner keyboard = new Scanner(System.in);

        String name = keyboard.nextLine();
        double fixedSalary = keyboard.nextDouble();
        double totalSales = keyboard.nextDouble();

        /* It calculates how much the salesperson should receive
        based on their fixed salary, plus a 15% bonus on sales
        made during the month.*/
        double totalSalary = fixedSalary + (totalSales * 0.15);

        System.out.printf("TOTAL = R$ %.2f\n", totalSalary);
    }
}
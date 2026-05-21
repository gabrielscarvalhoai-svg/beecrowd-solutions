import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main (String[] args) {

        Locale.setDefault(Locale.US);
        Scanner keyboard = new Scanner(System.in);

        int number = keyboard.nextInt();
        int hour = keyboard.nextInt();
        double hourly_value = keyboard.nextDouble();

        double salary = hour * hourly_value;

        System.out.printf("NUMBER = %d\n", number);
        System.out.printf("SALARY = U$ %.2f\n", salary);
    }
}

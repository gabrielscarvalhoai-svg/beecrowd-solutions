import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main (String[] args) {

        Locale.setDefault(Locale.US);
        Scanner keyboard = new Scanner(System.in);

        double A = keyboard.nextDouble();
        double B = keyboard.nextDouble();
        double C = keyboard.nextDouble();

        double MEDIA = ((A * 2.0) + (B * 3.0) + (C * 5.0)) / 10;

        System.out.printf("MEDIA = %.1f\n", MEDIA);
    }
}

import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main (String[] args) {

        Locale.setDefault(Locale.US);
        Scanner keyboard = new Scanner(System.in);

        double A = keyboard.nextDouble();
        double B = keyboard.nextDouble();

        double MEDIA = ((A * 3.5) + (B * 7.5)) / 11;

        System.out.printf("MEDIA = %.5f\n", MEDIA);
    }
}
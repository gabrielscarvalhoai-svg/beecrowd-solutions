import java.util.Scanner;

public class Main {
    public static void main (String[] args) {

        Scanner keyboard = new Scanner(System.in);

        int a = keyboard.nextInt();
        int b = keyboard.nextInt();

        int soma = a + b;

        System.out.printf("SOMA = %d\n", soma);

    }
}
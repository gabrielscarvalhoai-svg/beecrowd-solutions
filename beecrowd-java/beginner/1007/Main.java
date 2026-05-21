import java.util.Scanner;

public class Main {
    public static void main (String[] args) {

        Scanner keyboard = new Scanner(System.in);

        int A = keyboard.nextInt();
        int B = keyboard.nextInt();
        int C = keyboard.nextInt();
        int D = keyboard.nextInt();

        int DIFERENCA = (A * B) - (C * D);

        System.out.printf("DIFERENCA = %d\n", DIFERENCA);
    }
}
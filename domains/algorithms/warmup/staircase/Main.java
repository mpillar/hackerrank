import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        printStaircase(n);
    }

    public static void printStaircase(int n)
    {
        for (int i = 0; i < n; i++) {
            // Print spaces.
            for (int k = 0; k < n-i-1; k++) {
                System.out.print(' ');
            }

            // Print pound sequence.
            for (int k = 0; k < i+1; k++) {
                System.out.print("#");
            }

            System.out.println();
        }
    }
}
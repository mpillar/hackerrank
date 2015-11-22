import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        // If N is odd, print "Weird".
        // If N is even and, in between the range of 2 and 5(inclusive), print "Not Weird".
        // If N is even and, in between the range of 6 and 20(inclusive), print "Weird".
        // If N is even and N>20, print "Not Weird".
        String ans;
        if (n % 2 != 0) {
            ans = "Weird";
        } else if (n >= 2 && n <= 5) {
            ans = "Not Weird";
        } else if (n >= 6 && n <= 20) {
            ans = "Weird";
        } else {
            ans = "Not Weird";
        }

        System.out.println(ans);
    }

}
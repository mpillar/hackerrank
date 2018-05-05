import java.util.ArrayList;
import java.util.Scanner;

class LoopsII
{
    private static ArrayList<Integer> createSeries(int a, int b, int n)
    {
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int r = a;
            for (int j = 0; j < i+1; j++) {
                r += (1 << j) * b;
            }
            result.add(r);
        }
        return result;
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            ArrayList<Integer> series = createSeries(a, b, n);

            for (Integer s : series) {
                System.out.print(s);
                System.out.print(" ");
            }
            System.out.println();

        }

        in.close();
    }
}

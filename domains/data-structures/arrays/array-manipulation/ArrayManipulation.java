import java.util.Scanner;

public class ArrayManipulation
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        long[] array = new long[n+1];
        for (int i = 0; i < array.length; i++) {
            array[i] = 0;
        }

        for(long i = 0; i < m; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            long k = in.nextLong();

            array[a-1] += k;
            array[b] -= k;
        }

        long result = 0, current = 0;
        for (int i = 0; i < n; i++) {
            current += array[i];
            result = Math.max(result, current);
        }

        System.out.println(result);
    }
}

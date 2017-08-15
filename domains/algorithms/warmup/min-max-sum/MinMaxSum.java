import java.util.Scanner;

public class MinMaxSum
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int[] array = new int[5];
        for(int i = 0; i < 5; i++){
            array[i] = in.nextInt();
        }
        System.out.format("%d %d", minSumOfFour(array), maxSumOfFour(array));
    }

    private static long minSumOfFour(int[] array)
    {
        int largest = array[0];
        long sum = 0;

        for (int n : array) {
            sum += n;
            largest = Math.max(largest, n);
        }

        return sum - largest;
    }

    private static long maxSumOfFour(int[] array)
    {
        int smallest = array[0];
        long sum = 0;

        for (int n : array) {
            sum += n;
            smallest = Math.min(smallest, n);
        }

        return sum - smallest;
    }
}

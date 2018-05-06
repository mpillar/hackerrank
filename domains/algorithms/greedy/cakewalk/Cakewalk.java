import java.util.Arrays;
import java.util.Scanner;

public class Cakewalk {

    private static long marcsCakewalk(int[] calorie)
    {
        Arrays.sort(calorie);
        long result = 0;
        for (int i = 0; i < calorie.length; i++) {
            result += (1L << i) * calorie[calorie.length-i-1];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] calorie = new int[n];
        for(int calorie_i = 0; calorie_i < n; calorie_i++){
            calorie[calorie_i] = in.nextInt();
        }
        long result = marcsCakewalk(calorie);
        System.out.println(result);
        in.close();
    }
}

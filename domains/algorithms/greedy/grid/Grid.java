import java.util.Arrays;
import java.util.Scanner;

public class Grid {

    static String gridChallenge(String[] grid) {
        
        for (int i = 0; i < grid.length; i++) {
            char[] level = grid[i].toCharArray();
            Arrays.sort(level);
            grid[i] = String.valueOf(level);

            System.out.println(grid[i]);
        }
        
        String result = "YES";
        
        for (int row = 1; row < grid.length; row++) {
            for (int col = 0; col < grid.length; col++) {
                if (grid[row-1].charAt(col) > grid[row].charAt(col)) {
                    result = "NO";
                    break;
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        while (t > 0) {
            int n = in.nextInt();
            String[] grid = new String[n];
            for (int grid_i = 0; grid_i < n; grid_i++) {
                grid[grid_i] = in.next();
            }
            String result = gridChallenge(grid);
            System.out.println(result);

            t--;
        }

        in.close();
    }
}


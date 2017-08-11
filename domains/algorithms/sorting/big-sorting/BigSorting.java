import java.math.BigInteger;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class BigSorting
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] ints = new String[n];

        for (int i = 0; i < n; i++) {
            ints[i] = in.next();
        }

        Arrays.sort(ints, (String o1, String o2) -> {
            if (o1.length() != o2.length()) return o1.length() - o2.length();

            for (int i = 0; i < o1.length(); i++)
            {
                char left = o1.charAt(i);
                char right = o2.charAt(i);
                if (left != right) {
                    return (int) left - (int) right;
                }
            }

            return 0;
        });

        for (String s : ints) {
            System.out.println(s);
        }
    }
}
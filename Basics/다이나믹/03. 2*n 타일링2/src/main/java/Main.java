import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 22..
 */
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] cach = new int[input+1];

        cach[0] = 1;
        cach[1] = 3;

        for (int i=2; i<input; i++) {
            cach[i] = (cach[i-2]*2 + cach[i-1])%10007;
        }

        System.out.println(cach[input-1]);
    }
}

import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 27..
 */
public class 제곱수의합 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] cach = new int[input+1];
        cach[1] = 1;
        for (int i=1; i<=input; i++) {
            cach[i] = 1000;
            for (int j=1; j<=i; j++) {
                if (i-j*j >= 0) {
                    cach[i] = Math.min(cach[i - j*j] + 1, cach[i]);
                } else {
                    break;
                }
            }
        }

        System.out.println(cach[input]);
    }
}

import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 24..
 */
public class 쉬운계단수 {
    public static long mod = 1000000000L;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        long cach[][] = new long[num+1][10];

        for (int i=1; i<=9; i++) {
            cach[1][i] += 1;
        }

        for (int i=2; i<=num; i++) {
            for (int j=0; j<=9; j++) {
                cach[i][j] = 0;
                if (j-1>=0) cach[i][j] += cach[i-1][j-1];
                if (j+1<=9) cach[i][j] += cach[i-1][j+1];

                cach[i][j] %= mod;
            }
        }

        long answer = 0;

        for (int i=0; i<=9; i++) {
            answer += cach[num][i];
        }

        System.out.println(answer%mod);
    }
}

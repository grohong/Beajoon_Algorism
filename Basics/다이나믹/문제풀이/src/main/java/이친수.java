import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 24..
 */
public class 이친수 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        long[][] cach = new long[num+1][2];

        if (num != 1) {
            cach[2][0] = 1;
            cach[2][1] = 0;

            for (int i = 3; i <= num; i++) {
                cach[i][0] = cach[i - 1][0] + cach[i - 1][1];
                cach[i][1] = cach[i - 1][0];
            }
        }

        if (num == 1) {
            System.out.println(1);
        } else {
            System.out.println(cach[num][0] + cach[num][1]);
        }
    }
}

import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 30..
 */
public class 파도반수열 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int exam = scanner.nextInt();

        long[] cach = new long[101];
        cach[1] = 1;
        cach[2] = 1;
        cach[3] = 1;
        cach[4] = 2;
        for (int i=0; i<exam; i++) {
            int input = scanner.nextInt();
            for (int j=4; j<=input; j++) {
                if (cach[j] == 0) {
                    cach[j] = cach[j-2] + cach[j-3];
                }
            }

            System.out.println(cach[input]);
        }
    }
}

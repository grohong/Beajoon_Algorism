import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 24..
 */
public class 오르막수 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int[][] cach = new int[num+1][10];

        for (int i=0; i<=9; i++) {
            cach[1][i] = 1;
        }

        for (int i=2; i<=num; i++) {
            for (int j=0; j<=9; j++) {
                cach[i][j] = 0;
                for (int k=0; k<=j; k++) {
                    cach[i][j] += cach[i-1][k]%10007;
                }
            }
        }

        int answer = 0;
        for (int i=0; i<=9; i++) {
            answer += cach[num][i];
        }

        System.out.println(answer%10007);
    }
}

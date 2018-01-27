import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 27..
 */
public class 계단오르기 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] array = new int[input+1];
        for (int i=1; i<=input; i++) {
            array[i] = scanner.nextInt();
        }

        int[][] cach = new int[input+1][3];
        cach[1][1] = array[1];

        for (int i=2; i<=input; i++) {
            cach[i][1] = Math.max(cach[i-2][1], cach[i-2][2]) + array[i];
            cach[i][2] = cach[i-1][1] + array[i];
        }

        System.out.println(Math.max(cach[input][1], cach[input][2]));
    }
}

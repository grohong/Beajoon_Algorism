import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 26..
 */
public class 연속합 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] array = new int[input];
        for (int i=0; i<input; i++) {
            array[i] = scanner.nextInt();
        }

        int[] cach = new int[input];
        for (int i=0; i<input; i++) {
            cach[i] = array[i];
            if (i==0) continue;

            if (cach[i] < cach[i-1] + array[i]) {
                cach[i] = cach[i-1] + array[i];
            }
        }

        int answer = cach[0];
        for (int i=0; i<input; i++) {
            if (answer < cach[i]) {
                answer = cach[i];
            }
        }

        System.out.println(answer);
    }
}

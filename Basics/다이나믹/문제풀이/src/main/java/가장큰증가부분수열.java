import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 26..
 */
public class 가장큰증가부분수열 {
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

            for (int j=0; j<i; j++) {
                if (array[i] > array[j] && cach[i] < cach[j] + array[i]) {
                    cach[i] = cach[j] + array[i];
                }
            }
        }

        int answer = 0;
        for (int i=0; i<input; i++) {
            if (answer < cach[i]) {
                answer = cach[i];
            }
        }

        System.out.println(answer);
    }
}

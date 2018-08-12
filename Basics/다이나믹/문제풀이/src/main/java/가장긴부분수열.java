import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 26..
 */
public class 가장긴부분수열 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        int[] array = new int[length+1];

        for (int i=1; i<=length; i++) {
            array[i] = scanner.nextInt();
        }

        int[] cach = new int[length+1];
        for (int i=1; i<=length; i++) {
            cach[i] = 1;
            for (int j=1; j<i; j++) {
                if (array[j] < array[i] && cach[i] < cach[j]+1) {
                    cach[i] = cach[j] + 1;
                }
            }
        }

        int answer = 0;
        for (int i=1; i<cach.length; i++) {
            if (cach[i] > answer) {
                answer = cach[i];
            }
        }

        System.out.println(answer);
    }
}

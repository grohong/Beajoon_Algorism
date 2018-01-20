import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static int[] cach;

    public static int answer(int num) {
        if (num == 1) {
            return 0;
        }

        if (cach[num] > 0) {
            return cach[num];
        }

        cach[num] = answer(num-1) + 1;

        if (num%2 == 0) {
            int temp = answer(num/2) + 1;
            if (cach[num] > temp) {
                cach[num] = temp;
            }
        }

        if (num%3 == 0) {
            int temp = answer(num/3) + 1;
            if (cach[num] > temp) {
                cach[num] = temp;
            }
        }

        return cach[num];
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        cach = new int[input+1];

        System.out.println(answer(input));
    }
}

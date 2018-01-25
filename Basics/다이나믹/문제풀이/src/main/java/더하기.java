import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 22..
 * 1,2,3 더하기
 */
public class 더하기 {
    static int[] cach;

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        int inputCase = scanner.nextInt();
        cach = new int[13];

        cach[0] = 0;
        cach[1] = 1;
        cach[2] = 2;
        cach[3] = 4;

        for (int i=0; i<inputCase; i++) {
            System.out.println(getAnswer(scanner.nextInt()));
        }
    }

    public static int getAnswer(int input) {
        if (input == 3) {
            return cach[3];
        }

        if (input == 2) {
            return cach[2];
        }

        if (input == 1) {
            return cach[1];
        }

        if (cach[input-1] == 0) {
            cach[input-1] = getAnswer(input-1);
        }

        if (cach[input-2] == 0) {
            cach[input-2] = getAnswer(input-2);
        }

        if (cach[input-3] == 0) {
            cach[input-3] = getAnswer(input-3);
        }

        for (int i=3; i<input; i++) {
            cach[input] = cach[input-3] + cach[input-2] + cach[input-1];
        }

        return cach[input];
    }
}

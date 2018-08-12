import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 27..
 */
public class 타일채우기 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int num = 0;

        if (input%2 == 0) {
            num = input/2;
        }

        int[] cach = new int[num+1];
        cach[0] = 1;
        if (num > 0) {
            cach[1] = 3;
        }
        if (num > 1) {
            cach[2] = 11;
        }

        for (int i=3; i<=num; i++) {
            cach[i] = cach[i-1]*3;
            for (int j=0; j<i-1; j++) {
                cach[i] += cach[j]*2;
            }
        }

        if (num != 0) {
            System.out.println(cach[num]);
        } else {
            System.out.println("0");
        }
    }
}

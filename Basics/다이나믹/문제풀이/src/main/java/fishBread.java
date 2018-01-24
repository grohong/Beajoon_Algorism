import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 22..
 */
public class fishBread {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int leftBread = scanner.nextInt();
        int[] setPrice = new int[leftBread+1];

        for (int i=1; i<=leftBread; i++) {
            setPrice[i] = scanner.nextInt();
        }

        int[] cach = new int[leftBread+1];


        for (int i=1; i<=leftBread; i++) {
            for (int j=1; j<=i; j++) {
                if (cach[i] < cach[i-j] + setPrice[j]) {
                    cach[i] = cach[i-j] + setPrice[j];
                }
            }
        }

        System.out.println(cach[leftBread]);
    }
}

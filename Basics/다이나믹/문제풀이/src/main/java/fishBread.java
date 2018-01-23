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

        cach[0] = 0;
        cach[1] = setPrice[1]*leftBread;

        for (int i=2; i<=leftBread; i++) {
            if (setPrice[i] > cach[i-1] + setPrice[1]) {
                cach[i] = setPrice[i];
            } else {
                cach[i] = cach[i-1] + setPrice[1];
            }
        }

        System.out.println(cach[leftBread]);
    }
}

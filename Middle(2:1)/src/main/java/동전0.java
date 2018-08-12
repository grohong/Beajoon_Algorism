import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 3. 16..
 */
public class 동전0 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        int coinKinds = scanner.nextInt();
        int price = scanner.nextInt();

        int[] coin = new int[coinKinds];

        for (int i=0; i<coinKinds; i++) {
            coin[i] = scanner.nextInt();
        }

        int index = 0;
        int coinIndex = coinKinds-1;

        while (true) {
            if (price-coin[coinIndex]>=0) {
                price -= coin[coinIndex];
                index++;
            } else {
                coinIndex--;
            }

            if (coinIndex == -1) break;
            if (price == 0) break;
        }

        System.out.println(index);
    }
}

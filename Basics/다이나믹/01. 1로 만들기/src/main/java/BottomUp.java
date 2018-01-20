import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 20..
 */
public class BottomUp {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] cach = new int[input+1];
        cach[1] = 0;

        for (int i=2; i<input; i++) {
            cach[i] = cach[i-1] + 1;

            if (i%2 == 0 && cach[i] > cach[i/2] + 1) {
                
            }
        }
    }
}

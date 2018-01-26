import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 26..
 */
public class 가장긴바이오닉부분수열 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();

        int[] array = new int[input];
        int[] reverseArray = new int[input];
        for (int i=0; i<input; i++) {
            array[i] = scanner.nextInt();
            reverseArray[input-1-i] = array[i];
        }

        int[] increaseCach = new int[input];
        int[] decreaseCach = new int[input];

        for (int i=0; i<input; i++) {
            increaseCach[i] = 1;
            decreaseCach[i] = 1;
            for (int j=0; j<i; j++) {
                if (array[i] > array[j] && increaseCach[i] < increaseCach[j] + 1) {
                    increaseCach[i] = increaseCach[j] + 1;
                }

                if (reverseArray[i] > reverseArray[j] && decreaseCach[i] < decreaseCach[j] + 1) {
                    decreaseCach[i] = decreaseCach[j] + 1;
                }
            }
        }

        int answer = 0;
        for (int i=0; i<input; i++) {
            if (answer < increaseCach[i] + decreaseCach[input-1-i] - 1) {
                answer = increaseCach[i] + decreaseCach[input-1-i] - 1;
            }
        }

        System.out.println(answer);
    }
}

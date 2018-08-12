import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        int inputLength = input.length();

        String[] inputArray = new String[inputLength];

        for (int i=0; i<inputLength; i++) {
            inputArray[i] = input.substring(i);
        }

        Arrays.sort(inputArray);
        for (int i=0; i<inputLength; i++) {
            System.out.println(inputArray[i]);
        }
    }
}

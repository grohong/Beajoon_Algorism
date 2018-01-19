import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        StringBuilder result = new StringBuilder();

        for (int i=0; i<input.length(); i++) {
            char charator = input.charAt(i);

            if (charator >= 'a' && charator < 'n') {
                charator += 13;
            } else if (charator >= 'n' && charator <= 'z') {
                charator -= 13;
            } else if (charator >= 'A' && charator < 'N') {
                charator += 13;
            } else if (charator >= 'N' && charator <= 'Z') {
                charator -= 13;
            }

            result.append(charator);
        }

        System.out.println(result);
    }
}

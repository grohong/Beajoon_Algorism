import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String exam = scanner.nextLine();

        int[] alphabet = new int[26];
        for (int i=0; i<exam.length(); i++) {
            alphabet[exam.charAt(i) - 'a'] += 1;
        }

        for (int i=0; i<alphabet.length; i++) {
            System.out.print(alphabet[i]);
            System.out.print(" ");
        }
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String exam = bufferedReader.readLine();
        Stack<Character> left = new Stack<Character>();
        Stack<Character> right = new Stack<Character>();

        for (int i=0; i<exam.length(); i++) {
            left.push(exam.charAt(i));
        }

        int inputNum = Integer.parseInt(bufferedReader.readLine());

        while (inputNum-- > 0) {
            String[] command = bufferedReader.readLine().split(" ");
            char commandWhat = command[0].charAt(0);

            if (commandWhat == 'L' && left.size() != 0) {
                right.push(left.pop());
            }

            if (commandWhat == 'D' && right.size() != 0) {
                left.push(right.pop());
            }

            if (commandWhat == 'B' && left.size() != 0) {
                left.pop();
            }

            if (commandWhat == 'P') {
                char addWhat = command[1].charAt(0);

                left.push(addWhat);
            }
        }

        while (!left.empty()) {
            right.push(left.pop());
        }

        StringBuilder result = new StringBuilder();
        while (!right.empty()) {
            result.append(right.pop());
        }

        System.out.println(result);
    }
}

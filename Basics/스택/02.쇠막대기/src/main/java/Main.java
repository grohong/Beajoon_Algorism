import java.util.Scanner;
import java.util.Stack;

/**
 * Created by seonghohong on 2018. 1. 17..
 */
public class Main {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String exam = scanner.nextLine().trim();
        Stack<Character> examStack = new Stack<Character>();
        boolean lazerFlag = true;

        int barCount = 0;

        for (int i=0; i<exam.length(); i++) {
            if (exam.charAt(i) == '(') {
                examStack.push(exam.charAt(i));
                lazerFlag = true;
            } else {
                if (lazerFlag == true) {
                    barCount += examStack.size()-1;
                    examStack.pop();
                    lazerFlag = false;
                } else if (lazerFlag == false) {
                    barCount += 1;
                    examStack.pop();
                }
            }
        }

        System.out.println(barCount);
    }
}

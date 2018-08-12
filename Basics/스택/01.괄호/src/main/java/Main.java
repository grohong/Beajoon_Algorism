import java.util.Scanner;
import java.util.Stack;

/**
 * Created by seonghohong on 2018. 1. 17..
 */
public class Main {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int inputCase = scanner.nextInt();
        scanner.nextLine();
        while(inputCase-- > 0) {
            System.out.println(isVaild(scanner.nextLine()));
        }
    }

    public static String isVaild(String exam) {
        int examLength = exam.length();
        Stack<Character> examStack = new Stack<Character>();

        for(int i=0; examLength>i ; i++) {
            if (exam.charAt(i) == '(') {
                examStack.push(exam.charAt(i));
            } else {
                if (examStack.size() == 0 || examStack.peek() == ')') {
                    return "NO";
                } else if (examStack.peek() == '(') {
                    examStack.pop();
                }
            }
        }

        if (examStack.size() == 0) {
            return "YES";
        } else {
            return "NO";
        }
    }
}

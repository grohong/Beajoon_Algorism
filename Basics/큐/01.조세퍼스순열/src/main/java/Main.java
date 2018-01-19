import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        int peopleNum = scanner.nextInt();
        int josephNum = scanner.nextInt();

        StringBuilder result = new StringBuilder();
        Queue<Integer> queue = new LinkedList<Integer>();

        result.append("<");
        for (int i=1; i<=peopleNum; i++) {
            queue.add(i);
        }

        while (peopleNum > 0) {
            for (int i = 0; i < josephNum; i++) {
                if (i == josephNum - 1) {
                    result.append(queue.poll());
                    result.append(", ");
                    peopleNum--;
                } else {
                    queue.add(queue.poll());
                }
            }
        }

        result.deleteCharAt(result.length()-1);
        result.deleteCharAt(result.length()-1);
        result.append(">");

        System.out.println(result);
    }
}

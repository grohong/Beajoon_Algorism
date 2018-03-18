import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 3. 17..
 */
public class ATM {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> useTime = new ArrayList<Integer>();
        int people = scanner.nextInt();

        for (int i=0; i<people; i++) {
            useTime.add(scanner.nextInt());
        }

        Collections.sort(useTime);

        int answer = 0;
        int temp = 0;
        for (int i=0; i<people; i++) {
            temp += useTime.get(i);
            answer += temp;
        }

        System.out.print(answer);
    }
}

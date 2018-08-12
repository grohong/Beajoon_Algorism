import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 3. 18..
 */
public class 수묶기 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int one = 0;
        int zero = 0;
        ArrayList<Integer> plusNumber = new ArrayList<Integer>();
        ArrayList<Integer> miusNumber = new ArrayList<Integer>();
        int number = scanner.nextInt();

        for (int i=0; i<number; i++) {
            int temp = scanner.nextInt();

            if (temp > 1) {
                plusNumber.add(temp);
            } else if (temp < 0) {
                miusNumber.add(temp);
            } else if (temp == 0) {
                zero++;
            } else if (temp == 1) {
                one++;
            }
        }

        Collections.sort(plusNumber);
        Collections.reverse(plusNumber);
        Collections.sort(miusNumber);

        int answer = 0;

        for (int i=0; i<plusNumber.size(); i++) {
            int number1 = plusNumber.get(i);

            try {
                int number2 = plusNumber.get(i+1);
                answer += number1*number2;
                i++;
            } catch (Exception exception) {
                answer += number1;
                break;
            }
        }

        for (int i=0; i<miusNumber.size(); i++) {
            int number1 = miusNumber.get(i);

            try {
                int number2 = miusNumber.get(i+1);
                answer += number1*number2;
                i++;
            } catch (Exception exception) {
                if (zero==0) {
                    answer += number1;
                }
                break;
            }
        }

        answer += one;

        System.out.println(answer);
    }
}

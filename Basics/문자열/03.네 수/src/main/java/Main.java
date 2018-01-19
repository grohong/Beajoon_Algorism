import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 19..
 */
public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int num3 = scanner.nextInt();
        int num4 = scanner.nextInt();

        String addNum1 = ""+num1+""+num2+"";
        String addNum2 = ""+num3+""+num4+"";

        long result = Long.valueOf(addNum1) + Long.valueOf(addNum2);

        System.out.println(result);
    }
}

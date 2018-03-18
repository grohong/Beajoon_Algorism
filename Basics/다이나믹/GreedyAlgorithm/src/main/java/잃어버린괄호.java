import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 3. 18..
 */
public class 잃어버린괄호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        String[] minusInput = input.split("-");

        int answer = 0;

        try {
            answer = Integer.parseInt(minusInput[0]);
        } catch (NumberFormatException exception) {
            String[] plusInput = minusInput[0].split("\\+");
            int temp = 0;
            for (int j=0; j<plusInput.length; j++) {
                temp += Integer.parseInt(plusInput[j]);
            }

            answer = temp;
        }

        for (int i=1; i<minusInput.length; i++) {
            try {
                answer -= Integer.parseInt(minusInput[i]);
            } catch (NumberFormatException exception) {
                String[] plusInput = minusInput[i].split("\\+");
                int temp = 0;
                for (int j=0; j<plusInput.length; j++) {
                    temp += Integer.parseInt(plusInput[j]);
                }
                answer -= temp;
            }
        }

        System.out.println(answer);
    }
}

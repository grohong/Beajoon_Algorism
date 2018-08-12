import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by seonghohong on 2018. 1. 26..
 */
public class 터렛 {
    public static void main(String args[]) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int caseNum = Integer.valueOf(bufferedReader.readLine());

        while (caseNum-- > 0) {
            String[] inputValue = bufferedReader.readLine().split(" ");
            double[] input = new double[inputValue.length];

            for (int i=0; i<input.length; i++) {
                input[i] = Integer.valueOf(inputValue[i]);
            }

            double twoPointLength = Math.sqrt((input[0]-input[3])*(input[0]-input[3]) + (input[1]-input[4])*(input[1]-input[4]));
            double length = Math.sqrt((input[2]+input[5])*(input[2]+input[5]));

            if (twoPointLength==0) {
                if (input[2] == input[5]) System.out.println("-1");
                else System.out.println("0");
                continue;
            }

            if (twoPointLength+input[2] < input[5] || twoPointLength+input[5] < input[2]) {
                System.out.println("0");
                continue;
            }

            if (twoPointLength+input[2] == input[5] || twoPointLength+input[5] == input[2]) {
                System.out.println("1");
                continue;
            }

            if (twoPointLength > length) {
                System.out.println("0");
            } else if (twoPointLength == length) {
                System.out.println("1");
            } else if (twoPointLength < length){
                System.out.println("2");
            }
        }
    }
}

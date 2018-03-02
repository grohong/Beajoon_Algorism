import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 31..
 */
public class 암호코드 {
    public static int mod = 1000000;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        int[] cach = new int[input.length()];

        int startInt = Integer.parseInt(""+input.charAt(0)+""+""+input.charAt(1)+"");

        if (startInt == 10 && startInt == 20) {
            cach[0] = 1;
            cach[1] = 1;
        } else if (startInt <= 26 && startInt != 10 && startInt != 20) {
            cach[0] = 1;
            cach[1] = 2;
        } else if (startInt > 26 && startInt % 10 != 0) {
            cach[0] = 1;
            cach[1] = 1;
        } else {
            cach[0] = 0;
            cach[0] = 0;
        }


        for (int i=2; i<input.length(); i++) {
            int cachInt = Integer.parseInt(""+input.charAt(i-1)+""+""+input.charAt(i)+"");
            System.out.println("---------------------");
            System.out.println(cachInt);

            if (cachInt <= 26 && cachInt % 10 != 0) { cach[i] = (cach[i-1] + cach[i-2]) % mod; }
            else if (cachInt <= 26 && cachInt % 10 == 0) { cach[i] = (cach[i-1]) % mod; }
            else if (cachInt > 26 && cachInt % 10 != 0) { cach[i] = (cach[i-1]) % mod; }
            else {
                cach[i] = 0;
                break;
            }

            System.out.println("log");
            System.out.println(cach[i]);
            System.out.println("---------------------");
        }

        System.out.println(cach[input.length()-1]);
    }
}

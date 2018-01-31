import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 31..
 */
public class 암호코드 {
    public static int mod = 1000000;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        char[] inputString = input.toCharArray();

        int[] cach = new int[inputString.length+1];
        cach[0] = 1;
        cach[1] = 1;
        for (int i=2; i<=inputString.length; i++) {
            String temp = ""+inputString[i-2]+""+inputString[i-1]+"";

            int tempInt = Integer.parseInt(temp);
            if (tempInt == 0) {
                cach[i] = 0;
                continue;
            }

            if (tempInt == 30 || tempInt == 40 || tempInt == 50 || tempInt == 60 || tempInt == 70 || tempInt == 80 || tempInt == 90) {
                cach[i] = 0;
                continue;
            }

            if (1 <= tempInt && tempInt < 10) {
                cach[i] = cach[i-1];
            } else if (tempInt == 10) {
                cach[i] = cach[i-1] + 1;
            } else if (11 <= tempInt && tempInt <= 26) {
                cach[i] = (cach[i-1] + cach[i-2])%1000000;
            } else {
                cach[i] = cach[i-1];
            }
        }

        if (inputString[0] == '0') {
            System.out.println("0");
        } else if (inputString.length == 1) {
            System.out.println("1");
        } else if (inputString.length <= 2 && 27 <= Integer.parseInt(input) && Integer.parseInt(input) <= 99){
            System.out.println("1");
        } else {
            System.out.println(cach[inputString.length]);
        }

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        int n = s.length();
        s = " " + s;
        int[] d = new int[n+1];
        d[0] = 1;
        for (int i=1; i<=n; i++) {
            int x = s.charAt(i) - '0';
            if (1 <= x && x <= 9) {
                d[i] += d[i-1];
                d[i] %= mod;
            }
            if (i==1) {
                continue;
            }
            if (s.charAt(i-1) == '0') {
                continue;
            }
            x = (s.charAt(i-1)-'0')*10 + (s.charAt(i)-'0');
            if (10 <= x && x <= 26) {
                d[i] += d[i-2];
                d[i] %= mod;
            }
        }
        System.out.println(d[n]);
    }

//    public static void main(String args[]) {
//        Scanner sc = new Scanner(System.in);
//        String s = sc.nextLine().trim();
//        int n = s.length();
//        s = " " + s;
//        int[] d = new int[n+1];
//        d[0] = 1;
//        for (int i=1; i<=n; i++) {
//            int x = s.charAt(i) - '0';
//            if (1 <= x && x <= 9) {
//                d[i] += d[i-1];
//                d[i] %= mod;
//            }
//            if (i==1) {
//                continue;
//            }
//            if (s.charAt(i-1) == '0') {
//                continue;
//            }
//            x = (s.charAt(i-1)-'0')*10 + (s.charAt(i)-'0');
//            if (10 <= x && x <= 26) {
//                d[i] += d[i-2];
//                d[i] %= mod;
//            }
//        }
//        System.out.println(d[n]);
//    }
}

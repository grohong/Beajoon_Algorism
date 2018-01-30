import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 30..
 */
public class 합분배 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int inputN = scanner.nextInt();
        int inputK = scanner.nextInt();

        long[][] cach = new long[inputN+1][inputK+1];
        for (int i=1; i<=inputN; i++) {
            cach[i][1] = 1;
            for (int j=1; j<=inputK; j++) {
                cach[1][j] = j;
                if (i-1 > 0 && j-1>0) {
                    cach[i][j] = (cach[i - 1][j] + cach[i][j - 1])%1000000000;
                }
                System.out.println(""+i+", "+j+" "+cach[i][j]+"");
            }
        }

        System.out.println(cach[inputN][inputK]);
    }
}

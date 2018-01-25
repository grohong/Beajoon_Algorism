import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 1. 25..
 */
public class 포도주 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int wineNum = scanner.nextInt();
        int[] wineArray = new int[wineNum+1];

        for (int i=1; i<=wineNum; i++) {
            wineArray[i] = scanner.nextInt();
        }

        int[][] cach = new int[wineNum+1][3];
        for (int i=1; i<=wineNum; i++) {
            cach[i][0] = Math.max(cach[i-1][0],Math.max(cach[i-1][1], cach[i-1][2]));
            cach[i][1] = cach[i-1][0] + wineArray[i];
            cach[i][2] = cach[i-1][1] + wineArray[i];
        }

        int answer = Math.max(cach[wineNum][0], Math.max(cach[wineNum][1], cach[wineNum][2]));
        System.out.println(answer);
    }
}

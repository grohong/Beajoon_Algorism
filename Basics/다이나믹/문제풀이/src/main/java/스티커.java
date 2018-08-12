import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by seonghohong on 2018. 1. 25..
 */
public class 스티커 {
    public static void main(String[] args) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int examNum = Integer.valueOf(bufferedReader.readLine());

        while (examNum-- > 0) {
            int stickerNum = Integer.valueOf(bufferedReader.readLine());
            long[][] stickerArray = new long[stickerNum+1][2];

            String[] line1 = bufferedReader.readLine().split(" ");
            for (int i=1; i<=stickerNum; i++) {
                stickerArray[i][0] = Long.valueOf(line1[i-1]);
            }

            String[] line2 = bufferedReader.readLine().split(" ");
            for (int i=1; i<=stickerNum; i++) {
                stickerArray[i][1] = Long.valueOf(line2[i-1]);
            }

            long[][] cach = new long[stickerNum+1][3];
            for (int i=1; i<=stickerNum; i++) {
                cach[i][0] = Math.max(cach[i-1][0], Math.max(cach[i-1][1], cach[i-1][2]));
                cach[i][1] = Math.max(cach[i-1][0], cach[i-1][2]) + stickerArray[i][0];
                cach[i][2] = Math.max(cach[i-1][0], cach[i-1][1]) + stickerArray[i][1];
            }
            long answer = Math.max(cach[stickerNum][0], Math.max(cach[stickerNum][1], cach[stickerNum][2]));

            System.out.println(answer);
        }
    }
}

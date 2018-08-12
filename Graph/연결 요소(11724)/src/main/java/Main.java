import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String[] args) {
        int pointCount = valueGetter.getInt("정점의 개수");
        int lineCount = valueGetter.getInt("라인의 개수");

        ArrayList<Integer>[] pointLines = (ArrayList<Integer>[]) new ArrayList[pointCount+1];
        for (int i=1; i<=pointCount; i++) {
            pointLines[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<lineCount; i++) {
            int startPoint = valueGetter.getInt("시작점");
            int endPoint = valueGetter.getInt("끝점");

            pointLines[startPoint].add(endPoint);
            pointLines[endPoint].add(startPoint);
        }

        for (int i=1; i<=pointCount; i++) {
            Collections.sort(pointLines[i]);
        }

        boolean[] passPoint = new boolean[pointCount+1];
        int answer = 0;
        for (int i=1; i<=pointCount; i++) {
            if (passPoint[i] == false) {
                bfs(i, pointLines, passPoint);
                answer++;
                System.out.println("");
            }
        }
    }

    public static void bfs(int startPoint, ArrayList<Integer>[] pointLines, boolean[] passPoint) {
        if (passPoint[startPoint]) {
            return;
        }
        System.out.print(startPoint + " ");

        passPoint[startPoint] = true;
        for (int newStartPoint : pointLines[startPoint]) {
            if (passPoint[newStartPoint] == false) {
                bfs(newStartPoint, pointLines, passPoint);
            }
        }
    }
}

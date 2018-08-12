import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String[] args) {
        int pointCount = valueGetter.getInt("점의 개수");
        int lineCount = valueGetter.getInt("간선 개수");

        int startPoint = valueGetter.getInt("시작 점");

        ArrayList<Integer>[] pointLines = (ArrayList<Integer>[]) new ArrayList[pointCount+1];
        for (int i=1; i<=pointCount; i++) {
            pointLines[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<lineCount; i++) {
            int start = valueGetter.getInt("시작 점");
            int end = valueGetter.getInt("끝 점");

            pointLines[start].add(end);
            pointLines[end].add(start);
        }

        for (int i=1; i<=pointCount; i++) {
            Collections.sort(pointLines[i]);
        }

        boolean[] passPoint = new boolean[pointCount+1];
        dfs(startPoint, pointLines, passPoint);

        System.out.println("");

        passPoint = new boolean[pointCount+1];
        bfs(startPoint, pointLines, passPoint);
    }

    public static void dfs(int startPoint, ArrayList<Integer>[] pointLines, boolean[] passPoint) {
        if (passPoint[startPoint]) {
            return;
        }

        passPoint[startPoint] = true;
        System.out.print(startPoint + " ");
        for (int newStartPoint : pointLines[startPoint]) {
            if (passPoint[newStartPoint] == false) {
                dfs(newStartPoint, pointLines, passPoint);
            }
        }
    }

    public static void bfs(int startPoint, ArrayList<Integer>[] pointLines, boolean[] passPoint) {
        Queue<Integer> bfsQueue = new LinkedList<Integer>();
        bfsQueue.add(startPoint);
        passPoint[startPoint] = true;

        while (!bfsQueue.isEmpty()) {
            int newStartPoint = bfsQueue.remove();
            System.out.print(newStartPoint + " ");

            for (int endPoint : pointLines[newStartPoint]) {
                if (passPoint[endPoint] == false) {
                    passPoint[endPoint] = true;
                    bfsQueue.add(endPoint);
                }
            }
        }
    }
}

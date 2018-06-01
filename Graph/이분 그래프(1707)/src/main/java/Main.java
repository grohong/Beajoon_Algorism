import java.util.ArrayList;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int testCase = valueGetter.getInt("테스트 케이스");

        while (testCase-- > 0) {
            int point = valueGetter.getInt("점의 개수");
            int line = valueGetter.getInt("선의 개수");

            ArrayList<Integer>[] pointLines = (ArrayList<Integer>[]) new ArrayList[point+1];
            for (int i=1; i<=point; i++) {
                pointLines[i] = new ArrayList<Integer>();
            }

            for (int i=0; i<=line; i++) {
                int startPoint = valueGetter.getInt("출발점");
                int endPoint = valueGetter.getInt("도착점");

                pointLines[startPoint].add(endPoint);
                pointLines[endPoint].add(startPoint);
            }

            int[] colors = new int[point];
            boolean ok = true;

            for (int i=1; i<=point; i++) {
                if (color[i] == 0) {
                    dfs(pointLines, color, i, 1);
                }
            }


        }

    }

    public static void dfs(ArrayList<Integer>[] pointLines, int[] colors, int startPoint, int color) {
        colors[startPoint] = color;
        for (int newStartpoint : pointLines[startPoint]) {
            if (colors[newStartpoint] == 0) {
                dfs(pointLines, colors, newStartpoint, 3-color);
            }
        }
    }
}

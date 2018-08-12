import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int pointCount = valueGetter.getInt("좌표수");

        ArrayList<Point> pointList = new ArrayList<Point>();
        for (int i=0; i<pointCount; i++) {
            int[] setPoint = valueGetter.getIntArray(2, "좌표");
            Point point = new Point(setPoint[0], setPoint[1]);
            pointList.add(point);
        }

        Collections.sort(pointList);

        for (int i=0; i<pointCount; i++) {
            System.out.print(pointList.get(i).getX());
            System.out.println(" "+pointList.get(i).getY()+"");
        }
    }
}

class Point implements Comparable<Point> {
    private Integer X;
    private Integer Y;

    public Point(int x, int y) {
        this.X = x;
        this.Y = y;
    }

    public Integer getX() {
        return X;
    }

    public Integer getY() {
        return Y;
    }


    @Override
    public int compareTo(Point point) {
        if (X == point.getX()) {
            return Y.compareTo(point.getY());
        } else {
            return X.compareTo(point.getX());
        }
    }
}

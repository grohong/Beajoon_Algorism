import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int count = valueGetter.getInt("숫자 개수");
        int index = valueGetter.getInt("K번째 수");

        ArrayList<Integer> integers = new ArrayList<Integer>();
        for (int i=0; i<count; i++) {
            integers.add(valueGetter.getInt("숫자"));
        }

        Collections.sort(integers);
        System.out.println(integers.get(index-1));
    }
}

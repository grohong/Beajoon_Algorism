import java.util.Scanner;

public class Solution2 {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[] ) throws Exception {
        int testCase = valueGetter.getInt("테스트 케이스");

        for (int i=0; i<testCase; i++) {

        }
    }
}

class ValueGetter {

    Scanner scanner = new Scanner(System.in);

    public int[] getIntArray(int length, String what) {
        print(what);

        int[] intArray = new int[length];
        for (int i=0; i<length; i++) {
            intArray[i] = scanner.nextInt();
        }

        return intArray;
    }

    public int getInt(String what) {
        print(what);

        return scanner.nextInt();
    }

    public String getString(String what) {
        print(what);

        return scanner.next();
    }

    public void print(String what) {
        System.out.println(what);
    }
}
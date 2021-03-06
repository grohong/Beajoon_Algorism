import java.util.Scanner;

public class ValueGetter {

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

    public void print(String what) {
        System.out.println(what);
    }
}
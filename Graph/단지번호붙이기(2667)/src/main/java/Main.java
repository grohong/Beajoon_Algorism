import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Main {

    // Complete the missingWords function below.
    static String[] missingWords(String s, String t) {
        String[] sSplit = s.split(" ");
        String[] tSplit = t.split(" ");

        ArrayList<String> sStrings = new ArrayList<String>(Arrays.asList(sSplit));
        ArrayList<String> tStrings = new ArrayList<String>(Arrays.asList(tSplit));

        for (int i=0; i<tStrings.size(); i++) {
            if (sStrings.contains(tStrings.get(i))) {
                sStrings.remove(tStrings.get(i));
            }
        }

        String[] answer = new String[sStrings.size()];
        for (int i=0; i<sStrings.size(); i++) {
            answer[i] = sStrings.get(i);
        }

        return answer;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String t = scanner.nextLine();

        String[] res = missingWords(s, t);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(res[i]);

            if (i != res.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class Solution {
    private static final Scanner scanner = new Scanner(System.in);
    static String[] romanizer(int[] numbers) {
        String[] answer = new String[numbers.length];

        ArrayList<Roman> romans = new ArrayList<Roman>();
        Roman roman1000 = new Roman(1000, "M");
        Roman roman900 = new Roman(900, "CM");
        Roman roman500 = new Roman(500, "D");
        Roman roman400 = new Roman(400, "CD");
        Roman roman100 = new Roman(100, "C");
        Roman roman90 = new Roman(90, "XC");
        Roman roman50 = new Roman(50, "L");
        Roman roman40 = new Roman(40,"XL");
        Roman roman10 = new Roman(10, "X");
        Roman roman9 = new Roman(9, "IX");
        Roman roman8 = new Roman(8, "VIII");
        Roman roman7 = new Roman(7, "VII");
        Roman roman6 = new Roman(6, "VI");
        Roman roman5 = new Roman(5, "V");
        Roman roman4 = new Roman(4, "IV");
        Roman roman3 = new Roman(3, "III");
        Roman roman2 = new Roman(2, "II");
        Roman roman1 = new Roman(1, "I");

        romans.add(roman1000);
        romans.add(roman900);
        romans.add(roman500);
        romans.add(roman400);
        romans.add(roman100);
        romans.add(roman90);
        romans.add(roman50);
        romans.add(roman40);
        romans.add(roman10);
        romans.add(roman9);
        romans.add(roman8);
        romans.add(roman7);
        romans.add(roman6);
        romans.add(roman5);
        romans.add(roman4);
        romans.add(roman3);
        romans.add(roman2);
        romans.add(roman1);

        for (int i=0; i<numbers.length; i++) {

            ArrayList<String> romanAnswer = new ArrayList<String>();
            int number = numbers[i];

            for (int j = 0; j<romans.size(); j++) {

                if (number/romans.get(j).getNumber() != 0) {
                    int count = number/romans.get(j).getNumber();
                    Roman romanCase = romans.get(j);

                    for (int a = 0; a<count; a++) {

                        romanAnswer.add(romanCase.getRoman());
                    }
                    number = number%romans.get(j).getNumber();
                }
            }

            String temp = "";
            for (int b=0; b<romanAnswer.size(); b++) {
                temp = temp + romanAnswer.get(b);
            }

            answer[i] = temp;
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        int[] a = {75, 44, 33 ,21};


        String[]b =romanizer(a);

        for(String c: b){

            System.out.println(c);
        }


    }

    static class Roman {
        private Integer number;
        private String roman;

        public Roman(Integer number, String roman) {
            this.number = number;
            this.roman = roman;
        }

        public Integer getNumber() {
            return number;
        }

        public String getRoman() {
            return roman;
        }
    }
}
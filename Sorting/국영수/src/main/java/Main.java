import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int count = valueGetter.getInt("학생 수");

        ArrayList<Score> scores = new ArrayList<Score>();
        for (int i=0; i<count; i++) {
            String name = valueGetter.getString("학생 이름");
            int guk = valueGetter.getInt("국어");
            int eng = valueGetter.getInt("영어");
            int su = valueGetter.getInt("수학");

            Score score = new Score(name, guk, eng, su);
            scores.add(score);
        }

        Collections.sort(scores);

        for (int i=0; i<count; i++) {
            Score score = scores.get(i);
            System.out.println(""+score.getName()+"");
        }
    }

    static class Score implements Comparable<Score>{
        private String name;
        private Integer guk;
        private Integer eng;
        private Integer su;

        public Score(String name, int guk, int eng, int su) {
            this.name = name;
            this.guk = guk;
            this.eng = eng;
            this.su = su;
        }

        public String getName() {
            return name;
        }

        public Integer getGuk() {
            return guk;
        }

        public Integer getEng() {
            return eng;
        }

        public Integer getSu() {
            return su;
        }


        public int compareTo(Score score) {
            if (getGuk() == score.getGuk() && getEng() == score.getEng() && getSu() == score.getSu()) {
                return getName().compareTo(score.getName());
            } else if (getGuk() == score.getGuk() && getEng() == score.getEng()) {
                return getSu().compareTo(score.getSu())*-1;
            } else if (getGuk() == score.getGuk()) {
                return getEng().compareTo(score.getEng());
            } else {
                return getGuk().compareTo(score.getGuk())*-1;
            }
        }
    }
}

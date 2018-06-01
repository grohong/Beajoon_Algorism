import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int count = valueGetter.getInt("카드 개수");

        ArrayList<Card> cards = new ArrayList<Card>();
        ArrayList<Integer> cachs = new ArrayList<Integer>();
        for (int i=0; i<count; i++) {
            int number = valueGetter.getInt("카드");

            if (cachs.contains(number)) {
                int num = cachs.indexOf(number);
                cards.get(num).countCard();
            } else {
                cachs.add(number);
                Card card = new Card(number);
                cards.add(card);
            }
        }

        Collections.sort(cards);

        System.out.println(cards.get(0).getNumber());
    }

    static class Card implements Comparable<Card> {
        private Integer number;
        private Integer count = 1;

        public Card(int number) {
            this.number = number;
        }

        public Integer getCount() {
            return count;
        }

        public Integer getNumber() {
            return number;
        }

        public void countCard() {
            count++;
        }


        public int compareTo(Card card) {
            if (getCount() == card.getCount()) {
                return getNumber().compareTo(card.getNumber());
            } else {
                return getCount().compareTo(card.getCount())*-1;
            }
        }
    }
}

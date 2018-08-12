import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static ValueGetter valueGetter = new ValueGetter();

    public static void main(String args[]) {
        int count = valueGetter.getInt("이름 개수");

        ArrayList<Human> humans = new ArrayList<Human>();
        for (int i=0; i<count; i++) {
            int age = valueGetter.getInt("나이");
            String name = valueGetter.getString("이름");
            Human human = new Human(name, age, i);

            humans.add(human);
        }

        Collections.sort(humans);

        for (int i=0; i<count; i++) {
            Human human = humans.get(i);
            System.out.print(human.getAge());
            System.out.println(" "+human.getName()+"");
        }
    }
}

class Human implements Comparable<Human> {
    private String name;
    private Integer age;
    private Integer index;

    public Human(String name, Integer age, Integer index) {
        this.name = name;
        this.age = age;
        this.index = index;
    }

    public Integer getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public Integer getIndex() {
        return index;
    }

    public int compareTo(Human human) {
        if (age == human.getAge()) {
            return index.compareTo(human.getIndex());
        } else {
            return age.compareTo(human.getAge());
        }
    }
}

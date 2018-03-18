import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

/**
 * Created by seonghohong on 2018. 3. 16..
 */
public class 회의실배정 {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//
//        int conferenceNumber = scanner.nextInt();
//        int[][] conferenceTime = new int[conferenceNumber][2];
//
//        for (int i=0; i<conferenceNumber; i++) {
//            for (int j=0; j<2; j++) {
//                conferenceTime[i][j] = scanner.nextInt();
//            }
//        }
//
//        int[][] cach = new int[100000][2];
//
//        int index = 1;
//        cach[0] = conferenceTime[0];
//
//        for (int i=1; i<conferenceNumber; i++) {
//            int temp = index;
//
//            for (int j=0; j<temp; j++) {
//                if (conferenceTime[i][1] <= cach[j][0] || cach[j][1] <= conferenceTime[i][0]) {
//                    if (temp-1 == j) {
//                        index++;
//                        cach[temp] = conferenceTime[i];
//                    }
//                } else if ((cach[j][1]-cach[j][0]) >= (conferenceTime[i][1]-conferenceTime[i][0])) {
//                    if (conferenceTime[i][1] < cach[j][1]) {
//                        cach[j] = conferenceTime[i];
//                    }
//                }
//            }
//        }
//
//        System.out.println(index);
//    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int conferenceNumber = scanner.nextInt();
        ArrayList<Conference> conferenceTime = new ArrayList<Conference>();

        for (int i=0; i<conferenceNumber; i++) {
            int begin = scanner.nextInt();
            int end = scanner.nextInt();

            Conference conference = new Conference(begin, end);
            conferenceTime.add(conference);
        }

        Collections.sort(conferenceTime, new Comparator<Conference>() {
            public int compare(Conference o1, Conference o2) {
                if (o1.end == o2.end) {
                    if (o1.begin > o2.begin) {
                        return 1;
                    } else {
                        return -1;
                    }
                } else {
                    if (o1.end > o2.end) {
                        return 1;
                    } else {
                        return -1;
                    }
                }
            }
        });

        for (int i=0; i<conferenceNumber; i++) {
            System.out.println("-----------------------");
            System.out.println(conferenceTime.get(i).begin);
            System.out.println(conferenceTime.get(i).end);
        }

        int now = 0;
        int index = 0;

        for (int i=0; i<conferenceTime.size(); i++) {
            if (now <= conferenceTime.get(i).begin) {
                now = conferenceTime.get(i).end;
                index++;
            }
        }

        System.out.println(index);
    }
}

class Conference {
    int begin;
    int end;

    public Conference(int begin, int end) {
        this.begin = begin;
        this.end = end;
    }
}
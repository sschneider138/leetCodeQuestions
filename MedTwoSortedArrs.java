import java.util.ArrayList;
import java.util.PriorityQueue;

class MedTwoSortedArrs {

    public static void main(String[] args) {
        int[] arr1 = { 1, 2 };
        int[] arr2 = { 3, 4 };
        ArrayList<Integer> mergedArr = new ArrayList<>();

        PriorityQueue<Integer> pq1 = new PriorityQueue<>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<>();

        for (int num : arr1) {
            pq1.add(num);
        }

        for (int num : arr2) {
            pq2.add(num);
        }

        while (!pq1.isEmpty() && !pq2.isEmpty()) {
            if (pq1.peek() <= pq2.peek()) {
                mergedArr.add(pq1.poll());
            } else {
                mergedArr.add(pq2.poll());
            }
        }

        while (!pq1.isEmpty()) {
            mergedArr.add(pq1.poll());
        }

        while (!pq2.isEmpty()) {
            mergedArr.add(pq2.poll());
        }

        System.out.println(mergedArr);

        if (mergedArr.size() % 2 == 1) {
            System.out.println(mergedArr.get(mergedArr.size() / 2));
        } else {
            int mid1 = mergedArr.get(mergedArr.size() / 2 - 1);
            int mid2 = mergedArr.get(mergedArr.size() / 2);
            double avgMid = (mid1 + mid2) / 2.0;
            System.out.println(avgMid);
        }
    }
}

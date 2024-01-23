package leetCode;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class MergeArrs {
    ArrayList<Integer> arr1;
    ArrayList<Integer> arr2;
    PriorityQueue<Integer> pq1 = new PriorityQueue<>();
    PriorityQueue<Integer> pq2 = new PriorityQueue<>();
    ArrayList<Integer> mergedArr = new ArrayList<>();

    public MergeArrs(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {
        this.arr1 = arr1;
        this.arr2 = arr2;

        this.pq1.addAll(arr1);
        this.pq2.addAll(arr2);

    }

    public ArrayList<Integer> mergeArrs() {

        while (this.pq1.size() > 0 && this.pq2.size() > 0) {
            if (this.pq1.peek() < this.pq2.peek()) {
                this.mergedArr.add(this.pq1.poll());
            } else {
                this.mergedArr.add(this.pq2.poll());
            }
        }

        while (this.pq1.size() > 0 && this.pq2.size() == 0) {
            this.mergedArr.add(this.pq1.poll());
        }

        while (this.pq1.size() == 0 && this.pq2.size() > 0) {
            this.mergedArr.add(this.pq2.poll());
        }
        return this.mergedArr;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr1 = new ArrayList<>(List.of(1, 3, 5, 7, 9));
        ArrayList<Integer> arr2 = new ArrayList<>(List.of(2, 4, 6, 8, 10));

        MergeArrs testCode = new MergeArrs(arr1, arr2);
        System.out.println(testCode.mergeArrs());
    }

}
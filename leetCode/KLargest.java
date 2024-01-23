package leetCode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Arrays;

public class KLargest {
	ArrayList<Integer> inputArr;
	int k;

	public KLargest(ArrayList<Integer> inputArr, int k) {
		this.inputArr = inputArr;
		this.k = k;
	}

	public ArrayList<Integer> heapMethod() {
		ArrayList<Integer> storageArr = new ArrayList<>();
		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

		for (int num : inputArr) {
			pq.add(num);
		}

		for (int i = 0; i < k; i++) {
			storageArr.add(pq.poll());
		}

		return storageArr;

	}

	public static void main(String[] args) {
		ArrayList<Integer> inputArr = new ArrayList<>(Arrays.asList(1, 23, 12, 9, 30, 2, 50));

		KLargest obj = new KLargest(inputArr, 3);
		ArrayList<Integer> result = obj.heapMethod();
		System.out.println(result);
	}

}
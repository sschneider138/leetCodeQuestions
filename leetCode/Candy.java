package leetCode;

public class Candy {

	// leet code link: https://leetcode.com/problems/candy/

	public static void main(String[] args) {
		int[] ratings = new int[] { 1, 2, 2 };

		// edge case - no children in line
		if (ratings.length == 0) {
			System.out.println("no children in line");
		}

		int candyCount = ratings.length;

		// loop over arr
		for (int i = 0; i < ratings.length; i++) {
			int j = i - 1;
			int k = i + 1;

			// edge case - compare first kid with second kid
			if (i == 0) {
				if (ratings[i] > ratings[k]) {
					candyCount++;
				} else {
					continue;
				}

				// edge case - compare last kid with kid before him
			} else if (i == ratings.length - 1) {
				if (ratings[i] > ratings[j]) {
					candyCount++;
				} else {
					continue;
				}

				// normal cases - compare arbitrary kid with the kids on his immediate left and
				// right
			} else {
				if (ratings[j] < ratings[i] && ratings[i] > ratings[j]) {
					candyCount++;
				} else {
					continue;
				}
			}
		}

		// print num candy to hand out
		System.out.println(candyCount);
	}
}

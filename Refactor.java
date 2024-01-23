import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * goal of this is to generate a new array of elements that are ten times larger than the initial array
 * ex: [1, 2, 3] -> [10, 20, 30]
 */

public class Refactor {
    private ArrayList<Integer> arr;
    private ArrayList<Integer> newArr;

    public Refactor() {
        this.arr = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));
        this.newArr = new ArrayList<>();
    }

    // original method
    public void orignial() {
        int arrSize = this.arr.size();
        while (i < arrSize) {
            int tmp = this.arr.get(i);
            tmp = tmp * 10;
            this.newArr.add(i, tmp);
            i++;
        }
    }

    // refactored method - enhanced for loop with multiplication in ArrayList.add() method
    public void refactor() {
        for (int i : this.arr) {
            this.newArr.add(10 * i);
        }
    }

    public static void main(String[] args) {
        Refactor tst = new Refactor();
        System.out.println(tst.arr);
        tst.refactor();
        System.out.println(tst.newArr);

    }
}
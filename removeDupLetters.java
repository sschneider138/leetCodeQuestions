import java.util.HashSet;
import java.util.Set;

public class removeDupLetters {
    public static void main(String[] args) {
        String s = "cbacdcbc";

        Set<Character> set = new HashSet<>();

        for (char c : s.toCharArray()) {
            set.add(c);
        }

        System.out.println(set);
    }
}

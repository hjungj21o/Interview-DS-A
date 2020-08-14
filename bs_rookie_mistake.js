// You’re given a string containing letters of three types, R, B, and..

// R represents your current position, B represents a blocked position, and.represents an empty position.In one step, you can move to any adjacent position to your current position, as long as it is empty.Can you reach either the leftmost position or the rightmost position ?

//Return true if you can reach either the leftmost or the rightmost position, or false if you cannot.

//Example 1
// Input

// s = "......B....R.............."
// Output

// true

class Solution {
    solve(s) {
        // Write your code here
        let pos = s.indexOf("R");
        let left = pos - 1;
        let right = pos + 1;
        while (left >= 0 && right <= s.length - 1) {
            if (s[left] === ".") left--;
            if (s[right] === ".") right++;
            // if (s[left] === "B") left = pos;
            // if (s[right] === "B") right = pos;

            if (s[right] === "B" && s[left] === "B") return false;
        }

        return true;
    }
}
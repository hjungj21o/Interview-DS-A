// Given two strings S and T, return if they are equal when both are typed into empty text editors.# means a backspace character.

// Note that after backspacing an empty text, the text will continue empty.

// Example 1:

// Input: S = "ab#c", T = "ad#c"
// Output: true
// Explanation: Both S and T become "ac".
//     Example 2:

// Input: S = "ab##", T = "c#d#"
// Output: true
// Explanation: Both S and T become "".
//     Example 3:

// Input: S = "a##c", T = "#a#c"
// Output: true
// Explanation: Both S and T become "c".
//     Example 4:

// Input: S = "a#c", T = "b"
// Output: false
// Explanation: S becomes "c" while T becomes "b".

var backspaceCompare = function (S, T) {
    let stx1 = [];
    let stx2 = [];

    for (char of S) {
        if (char === "#") {
            stx1.pop();
        } else {
            stx1.push(char);
        }
    }

    for (char of T) {
        if (char === "#") {
            stx2.pop();
        } else {
            stx2.push(char);
        }
    };

    return stx1.join("") == stx2.join("");
};
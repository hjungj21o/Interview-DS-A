//Write a function that reverses a string.
//The input string is given as an array of characters char[].

//Do not allocate extra space for another array, 
//you must do this by modifying the input array in -place with O(1) extra memory.

//You may assume all the characters consist of printable ascii characters.



//Example 1:
//Input: ["h", "e", "l", "l", "o"]
//Output: ["o", "l", "l", "e", "h"]

//Example 2:
//Input: ["H", "a", "n", "n", "a", "h"]
//Output: ["h", "a", "n", "n", "a", "H"]


//my solution:
const reverseString = function (s) {
    const copy = s.slice(0);

    for (let i = 0; i < s.length; i++) {
        s[i] = copy[s.length - 1 - i]
    }
};

//other solutions:
const reverseString = function (s) {
    let begin = 0;
    let end = s.length - 1;

    while (end > begin) {
        [s[begin], s[end]] = [s[end], s[begin]];
        begin++;
        end--;
    }
};
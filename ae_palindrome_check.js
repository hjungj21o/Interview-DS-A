//Write a function that takes in a non-empty string and that returns a boolean
//represnting whether the string is a palindrome.


//my solution:
function isPalindrome(string) {
    // Write your code here.
    let bool = true;
    for (let i = 0; i < Math.floor(string.length); i++) {
        if (string[i] !== string[string.length - 1 - i]) bool = false;
    }
    return bool;
}

//Other solutions:
//O(n^2) time | O(n) space
function isPalindrome(string) {
    let reversedString = '';
    for (let i = string.length - 1; i >= 0; i--) {
        reversedString += string[i];
    }

    return string === reversedString;
}
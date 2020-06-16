//Write a function that takes in a non-empty string and that returns a boolean
//represnting whether the string is a palindrome.

function isPalindrome(string) {
    // Write your code here.
    let bool = true;
    for (let i = 0; i < Math.floor(string.length); i++) {
        if (string[i] !== string[string.length - 1 - i]) bool = false;
    }
    return bool;
}

// Do not edit the line below.
exports.isPalindrome = isPalindrome;

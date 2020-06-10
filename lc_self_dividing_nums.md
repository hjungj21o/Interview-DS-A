// A self-dividing number is a number that is divisible by every digit it conains.

// For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

// Also, a self-dividing number is not allowed to contain the digit zero.

// Given a lower and upper number bound, output a list of every possible self dividing number, 
// including the bounds if possible.

// Example 1:
// Input: 
// left = 1, right = 22
// Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

//iterate through the nums, starting from left, and ending at right, inclusive
//if it's less than 10, push into results array
//if larger than 10
    //helper function: 

var selfDividingNumbers = function(left, right) {
    const result = [];
    for (let i = left; i <= right; i++) {
        if (i % 10 !== 0 && digitalRoot(i)) {
            result.push(i)
        }
    }
    return result;
};

function digitalRoot(num) {
    // for (let i = num; i > 0; i % 10)
    let realNum = num; //21
    while (num > 0) {
        let mod = num % 10; // 2
        if (realNum % mod === 0) { //false
            if (num < 10) return true;
            num = Math.floor(num / 10); //num = 2
        } else {
            return false;
        }
    };
};

















var selfDividingNumbers = function(left, right) {
    const divisibleNums = [];

    for (let i = left; i <= right; i++) {
        if (divisibleNum(i) && i % 10 !== 0) divisibleNums.push(i);
    }

    return divisibleNums;
};

function divisibleNum(n) {
    const digits = [];
    let result = true;
    let m = n;

    while (m > 0) {
        const digit = m % 10
        digits.push(digit);
        m -= digit;
        m /= 10;
    }

    digits.forEach(d => {
        if (n % d !== 0) result = false; 
    })

    return result;
}
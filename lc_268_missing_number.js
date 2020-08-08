// Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

// Example 1:

// Input: [3, 0, 1]
// Output: 2
// Example 2:

// Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
// Output: 8

var missingNumber = function (nums) {
    let set = new Set();
    let count = 0;
    for (const num of nums) {
        set.add(num);
    }

    while (count < nums.length + 1) {
        if (!set.has(count)) return count;
        count++;
    }
    return -1;

};

var missingNumber = function (nums) {
    let expectedSum = 0;
    let realSum = 0;
    nums.forEach(num => realSum += num);

    for (let i = 0; i < nums.length + 1; i++) {
        expectedSum += i;
    }

    return expectedSum - realSum;

};

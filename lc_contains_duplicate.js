// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice in the 
// array, and it should return false if every element is distinct.

// Example 1:

// Input: [1, 2, 3, 1]
// Output: true

// Example 2:

// Input: [1, 2, 3, 4]
// Output: false

//let result variable initially point to false;
//create an obj that counts the number of element from input
//check if any of the counter is > 1
//if it is, flip result to true
//return result

var containsDuplicate = function (nums) {
    let result = false;
    const countNum = {};

    for (num of nums) {
        if (!countNum[num]) countNum[num] = 0
        countNum[num] ++;
    }

    Object.values(countNum).forEach(count => {
        if (count > 1) result = true;
    })

    return result;
};


//June's solution

var containsDuplicate = function (nums) {
    let result = false;
    const countNum = {};

    for (num of nums) {
        if (!countNum[num]) {
            countNum[num] = true
        } else {
            result = true;
        }
    }

    return result;
};
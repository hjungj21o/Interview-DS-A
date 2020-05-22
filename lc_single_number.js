//Given a non - empty array of integers, every element appears twice except 
//for one.Find that single one.

//Note: Your algorithm should have a linear runtime complexity.
//Could you implement it without using extra memory ?

//Example 1:
//Input: [2, 2, 1]
//Output: 1

//Example 2:

//Input: [4, 1, 2, 1, 2]
//Output: 4

//my solution:
var singleNumber = function (nums) {
    let obj = {};
    for (let i = 0; i < nums.length; i++) {
        if (!obj[nums[i]]) obj[nums[i]] = 0;
        obj[nums[i]] += 1;
    }

    for ([k, v] of Object.entries(obj)) {
        if (v === 1) return k;
    }
};
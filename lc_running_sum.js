// Given an array nums.We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.

var runningSum = function (nums) {
    const result = [];
    let runSum = 0;
    for (num of nums) {
        runSum += num;
        result.push(runSum);
    }

    return result;

};

var runningSum = function (nums) {
    for (let i = 1; i < nums.length; i++) {
        nums[i] += nums[i - 1]
    }

    return nums;

};
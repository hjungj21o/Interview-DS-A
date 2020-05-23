
//Write a function that takes in a non - empty array of distinct integers and an
//integer representing a target sum.If any two numbers in the input array sum
//up to the target sum, the function should return them in an array, in any
//order. If no two numbers sum up to the target sum, the function should return
//an empty array.

//Note that the target sum has to be obtained by summing two different integers
//in the array; you can't add a single integer to itself in order to obtain the
//target sum.

//You can assume that there will be at most one pair of numbers summing up to
//the target sum.


//my solution:
//O(n^2) time | O(1) space
function twoNumberSum(array, targetSum) {
    const result = [];

    for (let i = 0; i < array.length - 1; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] + array[j] === targetSum) {
                result.push(array[i], array[j])
            }
        }
    }
    return result;
    // Write your code here.
}

//Other solution
function twoNumberSum(array, targetSum) {
    const result = [];

    for (let i = 0; i < array.length - 1; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] + array[j] === targetSum) {
                result.push(array[i], array[j])
            }
        }
    }
    return result;
    // Write your code here.
}

//O(n) time | O(n) space
function twoNumberSum(array, targetSum) {
    // Write your code here.
    const nums = {};
    for (let i = 0; i < array.length; i++) {
        let num = array[i];
        let potentialMatch = targetSum - num
        if (nums[potentialMatch]) {
            return [potentialMatch, num];
        } else {
            nums[num] = true;
        }
    }
    return [];
}

function twoNumberSum(array, targetSum) {
    const sortedArr = array.sort((a, b) => a - b);
    let left = 0;
    let right = sortedArr.length - 1;

    while (left < right) {
        let currentSum = sortedArr[left] + sortedArr[right];
        if (currentSum === targetSum) {
            return [sortedArr[left], sortedArr[right]];
        } else if (currentSum < targetSum) {
            left++;
        } else if (currentSum > targetSum) {
            right--;
        };
    }
    return [];
}
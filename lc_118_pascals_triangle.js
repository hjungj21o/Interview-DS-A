// Given a non - negative integer numRows, generate the first numRows of Pascal's triangle.


// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 5
// Output:
// [
//     [1],
//     [1, 1],
//     [1, 2, 1],
//     [1, 3, 3, 1],
//     [1, 4, 6, 4, 1]
// ]

var generate = function (numRows) {
    if (!numRows) return [];
    if (numRows === 1) return [[1]];
    let result = [[1], [1, 1]];

    while (result.length < numRows) {
        let last = result[result.length - 1];
        let pushArr = [];
        for (let i = 0; i < last.length + 1; i++) {
            if (i === 0 || i === last.length) pushArr.push(1);
            else {
                let sum = last[i - 1] + last[i];
                pushArr.push(sum);
            }
        }
        result.push(pushArr);
    }
    return result;
};
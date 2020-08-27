// Given head which is a reference node to a singly - linked list.The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

// Return the decimal value of the number in the linked list.

// Example 1: 
// Input: head = [1, 0, 1]
// Output: 5
// Explanation: (101) in base 2 = (5) in base 10

// Example 2:

// Input: head = [0]
// Output: 0

var getDecimalValue = function (head) {
    let curr = head;
    let result = [];
    while (curr) {
        result.push(curr.val);
        curr = curr.next;
    }

    return parseInt(result.join(""), 2);
};

var getDecimalValue = function (head) {
    let curr = head;
    let result = 0;
    while (curr) {
        result = result * 2 + curr.val;
        curr = curr.next;
    }

    return result;
};
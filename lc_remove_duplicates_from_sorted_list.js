// Given a sorted linked list, delete all duplicates such that each element appear only once.

// Example 1:

// Input: 1 -> 1 -> 2
// Output: 1 -> 2

var deleteDuplicates = function (head) {
    let current = head;
    while (current && current.next) {
        if (current.val === current.next.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }

    return head;
};
// Given a linked list, remove the n - th node from the end of list and return its head.

//     Example:

// Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2.

// After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 -> 5.

var removeNthFromEnd = function (head, n) {

    let size = 1;
    let curr = head;
    while (curr.next) {
        curr = curr.next;
        size++;
    }

    let diff = size - n;

    let prev = null;
    curr = head;
    if (!diff) return head = head.next;
    while (diff) {
        prev = curr;
        curr = curr.next;
        diff--;
    }

    prev.next = prev.next.next;
    return head;
};

function removeKthNodeFromEnd(head, k) {
    // Write your code here.
    let first = head, second = head;

    while (k--) {
        first = first.next;
    }

    while (first && first.next) {
        first = first.next;
        second = second.next;
    }

    if (!first) {
        head = head.next;
    } else {
        second.next = second.next ? second.next.next : null;
    }

}
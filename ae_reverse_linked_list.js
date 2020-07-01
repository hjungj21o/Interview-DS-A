
// Reverse a singly linked list.

// Example:

// Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
// Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL


function reverseLinkedList(head) {
    // Write your code here.
    let p1 = null;
    let p2 = head;

    while (p2) {
        let p3 = p2.next;
        p2.next = p1;
        p1 = p2;
        p2 = p3;

    }

    return p1;
}
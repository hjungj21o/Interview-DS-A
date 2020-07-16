// Write a program to find the node at which the intersection of two singly linked lists begins.


var getIntersectionNode = function (headA, headB) {
    let nodes = new Set();
    let current = headA;

    while (current) {
        nodes.add(current);
        current = current.next;
    };

    current = headB;

    while (current) {
        if (nodes.has(current)) {
            return current;
        } else {
            current = current.next;
        }
    };
    return null;

};

//other answer

var getIntersectionNode = function (headA, headB) {
    let currentA = headA;
    let currentB = headB;

    while (currentA !== currentB) {
        currentA = currentA.next;
        currenbB = currentB.next;
        if(!currentA) currentA = headB;
        if(!currentB) currentB = headA;
    }

    return currentA;

}
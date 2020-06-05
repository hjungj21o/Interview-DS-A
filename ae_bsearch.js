
//O(n log(n)) time | O(log (n)) space
function binarySearch(array, target) {
    // Write your code here.
    if (array.length === 0) return -1;

    const mid = Math.floor(array.length / 2);
    let left = array.slice(0, mid);
    let right = array.slice(mid + 1);

    if (array[mid] === target) {
        return mid;
    } else if (array[mid] > target) {
        return binarySearch(left, target);
    } else if (array[mid] < target) {
        let result = binarySearch(right, target);
        return result === -1 ? -1 : result + mid + 1;
    }
}

//other solutions: 
//O (log(n)) time | O(log(n)) space

function binarySearch(array, target) {
    return binarySearchHelper(array, target, 0, array.length - 1);
}

function binarySearchHelper(array, target, left, right) {
    if (left > right) return -1;

    const middle = Math.floor((left + right) / 2);
    const potentialMatch = array[middle];

    if (target === potentialMatch) {
        return middle;
    } else if (target < potentialMatch) {
        return binarySearchHelper(array, target, left, middle - 1);
    } else {
        return binarySearchHelper(array, target, middle + 1, right);
    }
}

//O (log(n)) time | O(1) space 

function binarySearch(array, target) {
    return binarySearchHelper(array, target, 0, array.length - 1);
}

function binarySearchHelper(array, target, left, right) {
    while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        const potentialMatch = array[middle];

        if (target === potentialMatch) {
            return middle;
        } else if (target < potentialMatch) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}
//Write Mergesort
//Write a function that takes in an array of integers and returns a sorted version
//of that array. Use the Merge Sort algorithm to sort the array.
//[2,1,3,5,0]

function mergeSort(array) {
    if (array.length <= 1) return array;

    const mid = Math.floor(array.length / 2);
    const left = mergeSort(array.slice(0, mid));
    const right = mergeSort(array.slice(mid));

    return merged(left, right);
}

function merged(left, right) {
    const merged = [];

    while (left.length && right.length) {
        if (left[0] > right[0]) {
            merged.push(right.shift());
        } else {
            merged.push(left.shift());
        }
    }

    return merged.concat(left, right);
}

-Infinity
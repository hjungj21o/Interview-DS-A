// Given two non - empty arrays of integers, write a function that determines
// whether the second array is a subsequence of the first one.
// 
// 
// A subsequence of an array is a set of numbers that aren't necessarily adjacent
// in the array but that are in the same order as they appear in the array.
// For instance, the numbers form a subsequence of the array
// [1, 2, 3, 4], and so do the numbers[2, 4].
// Note that a single number in an array and the array itself are both valid
// subsequences of the array.

//my solution:
function isValidSubsequence(array, sequence) {
    // Write your code here.
    if (!array.length && sequence.length) return false;
    if (!sequence.length) return true;
    if (array[0] === sequence[0]) {
        return isValidSubsequence(array.slice(1), sequence.slice(1))
    } else {
        return isValidSubsequence(array.slice(1), sequence)
    }
}

//other solutions:
// O(n) time | O(1) space
function isValidSubsequence(array, sequence) {
    let arrIdx = 0;
    let seqIdx = 0;

    while (arrIdx < array.length && seqIdx < sequence.length) {
        if (array[arrIdx] === sequence[seqIdx]) seqIdx++;
        arrIdx++;
    }
    return seqIdx === sequence.length;
}

function findFirstDuplicate(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[Math.abs(arr[i]) - 1] < 0) {
            return Math.abs(arr[i]);
        } else {
            arr[Math.abs(arr[i]) -1] = -arr[Math.abs(arr[i]) -1]
        }
    }
    return -1;
}

console.log(findFirstDuplicate([1, 2, 4, 3, 2, 5, 1, 3]))
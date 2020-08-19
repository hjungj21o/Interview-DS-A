function findLongestSubarraySum(arr, target) {
    let result = [-1];
    let currSum = 0;
    let left = 0;
    let right = 0;
    
    while(right < arr.length) {
        currSum += arr[right];

        if (target === currSum) {
            if (result.length === 1) {
                result = [left + 1, right + 1]
            } else {
                if (result[1] - result[0] < right - left) result = [left + 1, right + 1]
            }
        }

        while (target < currSum) {
            currSum -= arr[left];
            left ++
        }

        right ++;
    }
}


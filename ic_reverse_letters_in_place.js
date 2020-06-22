//Write a function that takes an array of characters and reverses the letters in place.

// my solution: O(n) time | O(1) space
function reverse(arrayOfChars) {

    // Reverse the input array of characters in place
    for (let i = 0; i < Math.floor(arrayOfChars.length / 2); i++) {
        let temp = arrayOfChars[i];
        arrayOfChars[i] = arrayOfChars[arrayOfChars.length - 1 - i];
        arrayOfChars[arrayOfChars.length - 1 - i] = temp;
    }

}

//other solutions: 
function reverse(arrayOfChars) {

    let leftIndex = 0;
    let rightIndex = arrayOfChars.length - 1;

    while (leftIndex < rightIndex) {

        // Swap characters
        const temp = arrayOfChars[leftIndex];
        arrayOfChars[leftIndex] = arrayOfChars[rightIndex];
        arrayOfChars[rightIndex] = temp;

        // Move towards middle
        leftIndex++;
        rightIndex--;
    }
}
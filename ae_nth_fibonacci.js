
//The Fibonacci sequence is defined as follows: the first number of the sequence
//is "0", the second number is "1", and the nth number is the sum of the(n - 1)th
//and(n - 2)th numbers.
//Write a function that takes in an integer "n"  
//and returns the nth Fibonacci number.

//my solution
function getNthFib(n) {
    // Write your code here.
    if (n === 1) return 0;
    if (n === 2) return 1;

    let i = 2
    let base = [0, 1];
    while (i < n) {
        let secondLast = base[base.length - 2];
        let last = base[base.length - 1];
        base.push(secondLast + last);
        i++;
    }
    return base[base.length - 1];
}

// Other solutions
//O(2^n) time | O(n) space
function getNthFib(n) {
    if (n === 1) return 0;
    if (n === 2) return 1; 

    return getNthFib(n - 1) + getNthFib(n - 2);
}

//O(n) time | O(n) space
function getNthFib(n, memoize = {1: 0, 2: 1}) {
    if (n in memoize) {
        return memoize[n];
    } else {
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize);
        return memoize[n];
    }
}

//O(n) time | O(1) space
function getNthFib(n) {
    const lastTwo = [0, 1];
    let counter = 3;
    while (counter <= n) {
        const nextFib = lastTwo[0] + lastTwo[1];
        lastTwo[0] = lastTwo[1];
        lastTwo[1] = nextFib;
        counter ++;
    }
    return n > 1 ? lastTwo[1] : lastTwo[0];
}
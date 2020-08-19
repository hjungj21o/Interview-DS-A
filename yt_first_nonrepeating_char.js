function firstNonRepeatingChar(str) {
    const obj = {};

    for (const char of str) {
        obj[char] = obj[char] ? obj[char] + 1 : 1;
    }

    for (const char of str) {
        if (obj[char] === 1) return char;
    }

    return -1;
}

console.log(firstNonRepeatingChar("aaabcccdeeef"))
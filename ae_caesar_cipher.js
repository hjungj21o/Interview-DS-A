function caesarCipherEncryptor(string, key) {
    // Write your code here.
    const alpha = "abcdefghijklmnopqrstuvwxyz".split("");
    let result = "";
    for (let i = 0; i < string.length; i++) {
        let oldIdx = alpha.indexOf(string[i])
        let newIdx = oldIdx + key;
        let newChar = alpha[newIdx % 26];
        result += newChar;
    }
    return result;
}
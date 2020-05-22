//Have the function FindIntersection(strArr) read the array of strings stored 
//in strArr which will contain 2 elements: the first element will represent a 
//list of comma-separated numbers sorted in ascending order, the second element 
//will represent a second list of comma-separated numbers (also sorted). 
//Your goal is to return a comma-separated string containing the numbers that 
//occur in elements of strArr in sorted order. If there is no intersection, 
//return the string false.

//For example: if strArr contains["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] 
//the output should return "1,4,13" because those numbers appear in both 
//strings.The array given will not be empty, and each string inside the array 
//will be of numbers sorted in ascending order and may contain negative numbers.

//my solution:
function FindIntersection(strArr) {
    const elFirst = strArr[0].split(", ");
    const elSec = strArr[1].split(", ");

    const result = []
    for (let i = 0; i < elSec.length; i++) {
        if (elFirst.includes(elSec[i])) result.push(elSec[i]);
    };

    return result.length ? result.join(",") : false;

}

//other solutions: 
function FindIntersection(strArr) {
    const [firstEle, secondEle] = strArr.map(ele => ele.split(", "));

    const resultMap = {};
    const result = [];

    for (const num of firstEle) {
        resultMap[num] = true;
    }

    for (const num of secondEle) {
        if (resultMap[num]) result.push(num);
    }

    return result.lenght ? result.join(",") : false;
}

function FindIntersection(strArr) {

    const [a, b] = strArr.map(x => x.split(',').map(x => parseInt(x)));
    const s = new Set(b);

    return a.filter(x => s.has(x)).join(',') || 'false';
}
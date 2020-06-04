
//Write a function that takes in a "special" array and returns its product sum.
//A "special" array is a non - empty array that contains either integers or other
//"special" arrays.The product sum of a "special" array is the sum of its
//elements, where "special" arrays inside it are summed themselves and then
//multiplied by their level of depth.


function productSum(array, multiplier = 1) {
    // Write your code here.
    let result = 0;
    for (let i = 0; i < array.length; i++) {
        if (Array.isArray(array[i])) {
            result += productSum(array[i], multiplier + 1);
        } else {
            result += array[i];
        }
    }

    return result * multiplier;
}

//for (const element of array) => for loop
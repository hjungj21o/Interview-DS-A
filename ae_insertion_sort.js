function insertionSort(array){ //[1,3,4]

    for(let i = 1; i < array.length; i++){  
        let candidatePointer = i; 

        while(array[candidatePointer] < array[candidatePointer - 1] && candidatePointer - 1 >= 0){ 
            swap(array, candidatePointer, candidatePointer - 1); 
            candidatePointer--; 
        }
    }

    return array
}

function swap(array, index1, index2){
    [array[index1], array[index2]] = [array[index2], array[index1]]; 
}




function insertionSort(array) {
    for (let i = 1; i < array.length; i++) {
        let j = i;
        while (j > 0 && array[j - 1] > array[j]) {
            swap(j, j - 1, array);
            j --;
        }
    }
    return array;
}

function swap(i, j, array) {
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}
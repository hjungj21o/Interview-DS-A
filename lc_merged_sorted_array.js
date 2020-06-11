// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
// as one sorted array.

// Note:
// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space(size that is greater or equal to m + n) 
// to hold additional elements from nums2.

// Example:

// Input:
// nums1 = [1, 2, 3, 0, 0, 0], m = 3
// nums2 = [2, 5, 6], n = 3

// Output: [1, 2, 2, 3, 5, 6]

var merge = function (nums1, m, nums2, n) {
    //asssign nums from last empty spot in nums1
    //which one of the elements in nums 1 and nums 2 are greater?
    //pointer at end of nums 2
    //pointer at end of nums 1
    //pointer of at end of non-holding elements in nums1
    //p1(nums1 nonholding) = m - 1
    //p2 (nums2) = n - 1
    //p3 = (nums1.length - 1)  
    //while p1 and p2 >= 0
    //if (nums1[p1] > nums2[p2]) then nums1[p3] = nums1[p1], decrement p1
    //else, nums1[p3] = nums2[p2], decrement p2
    //decrement p3
    //[1, 2, 3, 0, 0, 0]
    //[4, 5, 6]
    let p1 = m - 1;
    let p2 = n - 1;
    let p3 = nums1.length - 1;

    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[p3] = nums1[p1];
            p1--;
        } else {
            nums1[p3] = nums2[p2];
            p2--;
        }
        p3--;
    }

    while (p2 >= 0) {
        nums1[p2] = nums2[p2];
        p2--;
    };

};


//concat nums1 and num2 so that there's one combined array, and sort array
//create a loop with m being the counter decrementing towards 0
//shift the result array until m hits 0 => get rid of the "hold elements" of nums1 array

//     nums1 + nums2;
//     nums1.sort((a, b) => a - b); //[0, 0, 0, 1, 2, 2, 3, 5, 6]

// //     while (n > 0) { //m = 0
// //         nums1.shift(); [0] //nums1 = [1, 2, 2, 3, 5, 6] shifted num = 0
// //         n --; //m = 0
// //     }

//     return nums1; //[1, 2, 2, 3, 5, 6]
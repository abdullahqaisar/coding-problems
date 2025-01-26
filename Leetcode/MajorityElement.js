/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let map = new Map();
    let maxNum = 0, maxCount = 0;

    for (let num of nums) {
        map.set(num, (map.get(num) || 0) + 1);

        if (map.get(num) > maxCount){
            maxNum = num;
            maxCount = map.get(num);
        }
    }

    return maxNum;
};

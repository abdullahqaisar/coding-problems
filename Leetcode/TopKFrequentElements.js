/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    // Using Sort Function
    count = {};

    for (let num of nums) {
        count[num] = (count[num] || 0) + 1;
    }

    const countArr = Object.entries(count).map(([num, freq]) => [freq, parseInt(num)]);
    countArr.sort((a, b) => b[0] - a[0]);

    return countArr.slice(0, k).map((pair) => pair[1]);

    // Using Bucket Sort
    const count = {};
    const freq = Array.from({ length: nums.length + 1 }, () => []);

    for (const n of nums) {
        count[n] = (count[n] || 0) + 1;
    }
    for (const n in count) {
        freq[count[n]].push(parseInt(n));
    }

    const res = [];
    for (let i = freq.length - 1; i > 0; i--) {
        for (const n of freq[i]) {
            res.push(n);
            if (res.length === k) {
                return res;
            }
        }
    }
};

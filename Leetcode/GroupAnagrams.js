/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const res = {};

    for (let str of strs) {
        const charCount = new Array(26).fill(0);

        for (let char of str) {
            charCount[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        if (!res[charCount]){
            res[charCount] = []
        }
        res[charCount].push(str);
    }

    return Object.values(res);
};

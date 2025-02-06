class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = "";
        for (let s of strs) {
            res += s.length + "#" + s;
        }

        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];

        let i = 0;
        while (i < str.length) {
            let j = i;
            while (str[j] !== '#') {
                j++;
            }

            const strLength = parseInt(str.substring(i, j));
            i = j + 1;
            j = strLength + i;

            res.push(str.substring(i, j));
            i = j;
        }

        return res;
    }
}

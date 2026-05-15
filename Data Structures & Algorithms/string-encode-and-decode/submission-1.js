class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        const encodedStrs = strs.map((str,idx) => {
            return str.length + "#" + str
        }).join("");
        return encodedStrs;
    }



    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const lenStrArr = str.length;
        let decodedStr = [];
        let i = 0;
        let lenCurrentStr = "";

        while(i < lenStrArr ){
            let currentChar = str[i]
            if(currentChar != "#"){
                lenCurrentStr += currentChar;
                i ++;
            }else {
                decodedStr.push(str.slice(i+1,i+1+Number(lenCurrentStr)));
                i += Number(lenCurrentStr) + 1;
                lenCurrentStr = "";
            }
        }
        return decodedStr;
    }

    
    
}

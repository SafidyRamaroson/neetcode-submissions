class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsUnique = new Set();
        const lenNum = nums.length;
        let  i = 0;

        while(i < lenNum) {
            numsUnique.add(nums[i]);
            i ++;
        }

        const lenNumsUnique = numsUnique.size;
        
        return lenNum != lenNumsUnique
    }
}

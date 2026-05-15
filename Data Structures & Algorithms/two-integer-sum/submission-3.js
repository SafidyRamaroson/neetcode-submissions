class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let def = 0;
        let i = 0;
        let res = [];
        while(i < nums.length){
            def = target - nums[i];
            let j = nums.lastIndexOf(def);
            if(j != -1 && j != i){
                res = [i,j]
                return res
            }else{
                i ++;
            }
        }
    }
}

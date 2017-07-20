
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] idx = new int[2];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i< nums.length; i++){
            if (map.containsKey(target - nums[i])) {
                idx[1] = i;
                idx[0] = map.get(target -nums[i]);
                return idx;
            }
            map.put(nums[i], i);
        }
        return idx;
    }
}

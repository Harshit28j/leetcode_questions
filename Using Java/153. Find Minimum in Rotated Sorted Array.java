public class Solution {
    public int findMin(int[] nums) {
        int s = 0;
        int end = nums.length - 1;
        
        while (s < end) {
            int mid = (s + end) / 2;
            
            if (nums[mid] > nums[end]) {
                s = mid + 1;
            } else {
                end--;
            }
        }
        
        return nums[s];
    }
}

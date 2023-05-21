class Solution {
    public boolean isPerfectSquare(int num) {
        if (num == 1) {
            return true;
        }
        
        int low = 1;
        int high = num;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            long sqr = (long) mid * mid;  // Use long to avoid overflow
            
            if (sqr == num) {
                return true;
            } else if (sqr < num) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return false;
    }
}

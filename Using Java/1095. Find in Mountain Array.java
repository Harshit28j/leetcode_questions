// Java implementation of the Find in Mountain Array problem
// assuming MountainArray class has get(int index) and length() methods

class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int lenArr = mountainArr.length();
        int peakIndex = findPeakIndex(mountainArr, lenArr);

        // search in the ascending half of the array
        int left = 0;
        int right = peakIndex;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (mountainArr.get(mid) == target) {
                return mid;
            } else if (mountainArr.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // search in the descending half of the array
        left = peakIndex;
        right = lenArr - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (mountainArr.get(mid) == target) {
                return mid;
            } else if (mountainArr.get(mid) < target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;  // target not found
    }

    private int findPeakIndex(MountainArray arr, int l) {
        int left = 0;
        int right = l - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr.get(mid) < arr.get(mid + 1)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}

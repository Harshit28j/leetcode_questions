public class Main {
    public static void main(String[] args) {
        int arr[]={0,-23,-321,-431,-500};
        int val=agnostic_bin(arr,-500);
        System.out.println(val);
    }
    static int agnostic_bin(int[] arr,int tar){
        int start=0,mid;
        int end=arr.length-1;
        boolean isAsc=(arr[start]<arr[end]);
        while (start<=end) {
            mid = start + (end - start) / 2;
            if (isAsc) {
                if (tar > arr[mid]) {
                    start = mid + 1;
                } else if (tar < arr[mid]) {
                    end = mid - 1;
                } else {
                    return (mid);
                }
            } else {
                if (tar < arr[mid]) {
                    start = mid + 1;
                } else if (tar > arr[mid]) {
                    end = mid - 1;
                } else {
                    return (mid);
                }
            }
        }
        return(-1);
    }
}

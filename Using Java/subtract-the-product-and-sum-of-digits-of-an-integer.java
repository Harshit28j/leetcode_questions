class Solution {
    public int subtractProductAndSum(int n) {
        int s_d,mul=1;
        int d_sum=0;
        while(n!=0){
            s_d=n%10;
            mul=mul*s_d;
            d_sum+=s_d;
            n=n/10;
        }
        return(mul-d_sum);
    }
}
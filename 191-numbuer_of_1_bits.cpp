class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        for (int i = 31; i >= 0; i--){
            if (n >= pow(2, i)){
                cnt ++;
                n -= pow(2, i);
            }
        }
     return cnt;           
    }
};

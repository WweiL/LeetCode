// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int ans = 0;
        // recursive view:
        // base case: one of n, read4(buf) is less than 4, return the minimun
        // then recurse
        while(n > 0){
            int tmp = min(read4(buf), n);
            if(tmp < 4){
                return ans + tmp;
            }
            buf += 4;
            ans += 4;
            n -= 4;
        }
        return ans;
    }
};

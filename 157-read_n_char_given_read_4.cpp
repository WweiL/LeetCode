// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    /**
     * Given a file = "abc", and a destination buffer, buf = ["", "", "", ..... ]
     * after calling read(buf, 4), we will have: output = 3
     * and the destination buffer becomes buf = ["a", "b", "c", "", "", "", .......]
     * Because the read(buf, 4) function copied 4 characters (but there are only 3 in the file) from the file
     * into the destination buffer
     */
    int read(char *buf, int n) {
        int ans = 0;
        // recursive view:
        // base case: one of n, read4(buf) is less than 4, return the minimun
        // then recurse
        // "abc", 5
        // "abcde" 1
        // while(n > 0){
        //     int retVal = read4(buf+ans);
        //     if(retVal == 0)
        //         break;
        //     if(n > retVal){
        //         n -= retVal;
        //         ans += retVal;
        //     }
        //     else{
        //         ans += n;
        //         break;
        //     }
        // }
        while(n > 0){
            int retVal = min(read4(buf+ans), n);
            if(retVal == 0)
                break;
            n -= retVal;
            ans += retVal;
        }
        return ans;
    }
};
